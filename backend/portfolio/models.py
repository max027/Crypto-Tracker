from django.db import models
from django.contrib.auth.models import User

class OrderHistory(models.Model):
    order_type=models.CharField(max_length=20,blank=True,null=True )
    order_price=models.DecimalField(decimal_places=20,max_digits=30,blank=True,null=True)
    coin_name=models.CharField(max_length=20,blank=True,null=True)
    order_qty=models.IntegerField(blank=True,null=True)

class Portfolio(models.Model):
    coin_name=models.CharField(max_length=20 ,blank=True,null=True)
    coin_qty=models.IntegerField(blank=True,null=True)
    total_investment=models.DecimalField(decimal_places=10,max_digits=20,null=True)




