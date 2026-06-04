from django.db import models

# Create your models here.
# this for the link the pgadmin to the producet what it required 

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    image=models.ImageField(upload_to ='products/',blank=True,null=True)
    

    def __str__(self):
        return self.name
    


#this for the review table link to the pgadmin

from django.db import models

class Review(models.Model):
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    title = models.CharField(max_length=200, blank=True)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



# from django.db import models

# class Product(models.Model):
#     name = models.CharField(max_length=200)
#     price = models.FloatField()
#     image = models.ImageField(upload_to='products/')

#     def average_rating(self):
#         reviews = self.reviews.all()
#         if reviews.count() == 0:
#             return 0
#         return round(sum(r.rating for r in reviews) / reviews.count(), 1)

#     def __str__(self):
#         return self.name


# class Review(models.Model):
#     product = models.ForeignKey(
#         Product,
#         related_name="reviews",
#         on_delete=models.CASCADE
#     )
#     name = models.CharField(max_length=100)
#     rating = models.IntegerField()  # ⭐ 1–5
#     title = models.CharField(max_length=200)
#     comment = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)