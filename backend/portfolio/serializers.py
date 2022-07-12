from dataclasses import fields
from rest_framework.serializers import ModelSerializer 
from .models import  OrderHistory

class OrderHistorySerializers(ModelSerializer):
    class Meta:
        model=OrderHistory
        fields='__all__'