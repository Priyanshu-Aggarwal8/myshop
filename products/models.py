from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=150)

    def __str__(self):
        return f"{self.title}"

class Address(models.Model):
    street = models.CharField(max_length = 30)
    zipcode = models.SmallIntegerField(max_length= 10)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

class Brand(models.Model):
    title = models.CharField(max_length=50)
    logo = models.ImageField(blank=True, upload_to="brand-logo")
    address = models.OneToOneField(Address, on_delete=models.DO_NOTHING, null = True)

    def __str__(self):
        return f"{self.title}"
    
class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    category = models.ManyToManyField(Category)
    image = models.ImageField(blank=True, upload_to="product-img")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null = True)
    price = models.PositiveIntegerField()
    slug = models.SlugField(blank=True)
    isBestseller = models.BooleanField(default = False)
    suggestions = models.ManyToManyField('self')

    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.slug = self.id 
        super().save(*args, **kwargs)

class Feedback(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    description = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.product}"