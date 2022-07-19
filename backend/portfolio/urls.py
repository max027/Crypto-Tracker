from django.urls import path,include
from .views import getorder,updateorder,getportfolio,updateportfolio
urlpatterns = [
    path('getorder/',getorder ),
    path('updateorder/',updateorder),
    path('getportfolio/',getportfolio),
    path('updateportfolio/',updateportfolio),
]

