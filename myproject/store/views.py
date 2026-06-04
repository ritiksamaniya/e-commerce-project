

from django.shortcuts import render, get_object_or_404
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})

def search_results(request):
    query = request.GET.get('q')
    products = Product.objects.filter(name__icontains=query) if query else []
    return render(request, 'store/search_result.html', {
        'products': products,
        'query': query
    })

from django.core.paginator import Paginator

def search_results(request):
    query = request.GET.get('q')
    product_list = Product.objects.filter(name__icontains=query) if query else []

    paginator = Paginator(product_list, 5)  # ✅ 5 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'store/search_result.html', {
        'query': query,
        'page_obj': page_obj,
    })





from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import Product, Review

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    # ✅ HANDLE REVIEW SUBMISSION
    if request.method == "POST":
        Review.objects.create(
            product=product,
            name=request.POST.get("name"),
            rating=int(request.POST.get("rating")),  # convert to int
            title=request.POST.get("title"),
            comment=request.POST.get("comment"),
        )
        messages.success(request, "Review submitted successfully!")
        return redirect('product_detail', pk=product.pk)

    # ✅ FETCH REVIEWS
    reviews = Review.objects.filter(product=product).order_by('-id')
    review_count = reviews.count()

    # ALL reviews queryset
    all_reviews = Review.objects.filter(product=product).order_by('-id')

    # 👇 ONLY FIRST 3 REVIEWS FOR PRODUCT PAGE
    reviews = all_reviews[:3]

    review_count = all_reviews.count()

    # ✅ CALCULATE AVERAGE RATING
    if review_count > 0:
        total_rating = sum(review.rating for review in reviews)
        average_rating = round(total_rating / review_count, 1)
    else:
        average_rating = 0

    return render(request, 'store/product_detail.html', {
        'product': product,
        'reviews': reviews,
        'average_rating': average_rating,  # 👈 PASS AVG
        'review_count': review_count,      # 👈 PASS COUNT
    })


# def all_reviews(request, pk):
#     product = get_object_or_404(Product, pk=pk)

#     reviews_list = Review.objects.filter(product=product).order_by('-id')

#     # ✅ PAGINATION (5 reviews per page)
#     paginator = Paginator(reviews_list, 5)
#     page_number = request.GET.get('page')
#     reviews = paginator.get_page(page_number)

#     return render(request, 'store/all_reviews.html', {
#         'product': product,
#         'reviews': reviews,
#     })

from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from .models import Product, Review

def all_reviews(request, pk):
    product = get_object_or_404(Product, pk=pk)

    # ✅ FULL QUERYSET (DO NOT SLICE)
    reviews_queryset = Review.objects.filter(product=product).order_by('-id')

    # ✅ PAGINATOR (5 REVIEWS PER PAGE)
    paginator = Paginator(reviews_queryset, 5)

    # ✅ GET PAGE NUMBER FROM URL
    page_number = request.GET.get('page')

    # ✅ THIS LINE DOES THE MAGIC
    reviews = paginator.get_page(page_number)

    return render(request, 'store/all_reviews.html', {
        'product': product,
        'reviews': reviews,
    })