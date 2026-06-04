
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_results, name='search_results'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/<int:pk>/reviews/', views.all_reviews, name='all_reviews'),
]
