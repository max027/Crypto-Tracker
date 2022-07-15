from django.urls import path,include
from .views import getorder,updateorder
urlpatterns = [
    path('getorder/',getorder ),
    path('updateorder/',updateorder),
]

