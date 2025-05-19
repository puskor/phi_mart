from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator,MaxValueValidator
# from cloudinary.models import CloudinaryField


class Category(models.Model):
    name=models.CharField(max_length=70)
    description = models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name=models.CharField(max_length=100)
    description= models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name="products")
    create_at =models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-id',]
       
    
    def __str__(self):
        return self.name
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name="product_image")
    # image = CloudinaryField('image')
    
class review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating =models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    comment= models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=False)
    
    def __str__(self):
        return f"Review by {self.user.first_name} in {self.product.name}"