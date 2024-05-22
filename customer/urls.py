from django.urls import path,include
from .views import *

urlpatterns = [
    path('',Index.as_view(),name='index'),
    path('accounts/',include('allauth.urls')),
    path('about/', About.as_view(),name ='about'),
    path('order/',Order.as_view(),name='order'),
    path("menu/<str:category>/", GetMenuByCategory.as_view()),
    path("menu/", GetMenu.as_view(), name="menu")
]
