from django.db import models

# Create your models here.

class tables(models.Model):
    title=models.CharField(max_length=100,blank=False)
    des=models.CharField(max_length=100,blank=False)
    images=models.ImageField(upload_to='table/',blank=False)

class productlist(models.Model):
    brand=models.CharField(max_length=100,blank=False)
    price=models.CharField(max_length=100,blank=False)
    category=models.CharField(max_length=100,blank=True,null=True)
    images=models.ImageField(upload_to='productlist/',blank=False)
    description=models.TextField(max_length=2000,blank=False)

    

class subscribe(models.Model):
    email=models.EmailField(max_length=100,blank=False)

class getID(models.Model):
    id1=models.IntegerField(blank=False) 
class shoping_cart1(models.Model):

   

    atm = models.CharField(max_length=16)

    cvv = models.CharField(max_length=3)

    amount = models.IntegerField(max_length=10)

    help = models.CharField(max_length=50)
    