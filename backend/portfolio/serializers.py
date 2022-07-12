from dataclasses import fields
from rest_framework import serializers
from .models import  OrderHistory

class OrderHistorySerializers(serializers.ModelSerializer):
    class Meta:
        model=OrderHistory
        fields=(
            'user_name',
            'order_type',
            'order_price',
            'coin_name',
            'order_date',
            'order_qty'
        )