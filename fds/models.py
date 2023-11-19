from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserType(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    type = models.CharField(max_length=50,null=True)

class customers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    address = models.CharField(max_length=50,null=True)
    phone = models.CharField(max_length=50,null=True)

class agents(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    address = models.CharField(max_length=50,null=True)
    phone = models.CharField(max_length=50,null=True)
    image = models.ImageField(null=True)

class products(models.Model):
    name = models.CharField(max_length=100,null=True)
    category = models.CharField(max_length=100,null=True)
    price = models.CharField(max_length=100,null=True)
    image = models.ImageField(null=True)
    status = models.CharField(max_length=100,null=True)   

class cart(models.Model):
    product = models.ForeignKey(products, on_delete=models.CASCADE,null=True)
    customer = models.ForeignKey(customers, on_delete=models.CASCADE,null=True)
    quantity = models.IntegerField(null=True)
    status=models.CharField(max_length=50,null=True)
    payment=models.CharField(max_length=50,null=True)
    total = models.CharField(max_length=100,null=True)

class assign(models.Model):
    crt = models.ForeignKey(cart, on_delete=models.CASCADE,null=True)
    agent = models.ForeignKey(agents, on_delete=models.CASCADE,null=True)
    status=models.CharField(max_length=50,null=True)
    