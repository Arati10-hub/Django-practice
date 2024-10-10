from django.db import models


class ProductCustomManager(models.Manager):
     def get_queryset(self):
          return super().get_queryset()  #to get all object
     

     def royalCanin(self):
          return super().get_queryset().filter(product_brand="Royal Canin")
     

     def drools(self):
          return super().get_queryset().filter(product_brand="Drools")

# Create your models her

#create class which inherits Model class from models.

#first install pillow for that use ______ pip install pillow
#then write below code
#primary key automatically made that's id
class Product(models.Model):
    product_name=models.CharField(max_length=100,null=False)
    product_description=models.TextField(default="product description")
    product_price=models.PositiveIntegerField(default=0)
    product_image=models.ImageField(upload_to="products/")  # image folder path gives into upload_to
    product_brand=models.CharField(max_length=100,default="superpet")

    
    # aish=models.Manager()
    customManager=ProductCustomManager()
    

    def __str__(self):
         return self.product_name



  
        






#manage media files(djangocentral on web)
#steps:-
#1.open settings.py
class Category(models.Model):
    pass
