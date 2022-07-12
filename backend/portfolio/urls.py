from django.urls import path,include
from .views import getorder
urlpatterns = [
    path('orderhistory/',getorder ),
]

