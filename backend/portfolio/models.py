from curses.ascii import US
from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User

class OrderHistory(models.Model):
    order_choice=(
        ('B','BUY'),
        ('S','SELL')
    )
    user_name=models.ForeignKey(User,on_delete=models.CASCADE)
    order_type=models.CharField(max_length=20,choices=order_choice)
    order_price=models.DecimalField(decimal_places=10,max_digits=20)
    coin_name=models.CharField(max_length=20)
    order_date=models.DateTimeField(auto_now_add=TRUE)
    order_qty=models.IntegerField()

class Portfolio_coin(models.Model):
    coin_name=models.CharField(max_length=20)
    coin_qty=models.IntegerField()
    total_investment=models.DecimalField(decimal_places=10,max_digits=20)

class Portfolio(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    coin=models.ForeignKey(Portfolio_coin,on_delete=models.CASCADE)



