from django.db import models
from django.utils.text import slugify


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs) 

    def __str__(self):
        return self.name

class T_shirts(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    slug =  models.SlugField(unique=True, blank=True)
    type = models.ForeignKey(Category, on_delete=models.CASCADE)
    character = models.TextField()
    UZ = "so'm"
    RU = '₽'
    ENG = '$'
    the_price = {
        (UZ, "so'm"),
        (RU, "₽"),
        (ENG, "$"),
    }
    price_type = models.CharField(max_length=10, choices=the_price, default=UZ)
    price = models.IntegerField()
    image = models.ImageField()


    def __str__(self):
        return self.name


class Buy(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    products = models.ForeignKey(T_shirts, on_delete=models.CASCADE, null=True)
    ALL_SIZE = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Extra Large')      
    )
    size = models.CharField(max_length=100, choices=ALL_SIZE, default='M')
    ALL_VALUES = (
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5"),
    )
    how = models.CharField(max_length=100, choices=ALL_VALUES, default="1")
    map = models.TextField()
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name


class Avertising(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    image = models.ImageField()


    def __str__(self):
        return self.name
    
class Register(models.Model):
    name =  models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name