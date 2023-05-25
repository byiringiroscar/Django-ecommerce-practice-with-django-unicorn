from django.urls import path

from  . views import *

urlpatterns = [
    path('', home, name="home"),
    path('shop/', shop, name="shop")
]