from django.contrib import admin
from .models import Portfolio,Portfolio_coin,OrderHistory

admin.site.register(Portfolio_coin)
admin.site.register(Portfolio)
admin.site.register(OrderHistory)
