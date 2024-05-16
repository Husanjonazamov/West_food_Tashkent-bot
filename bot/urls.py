from django.urls import path

from . import views

urlpatterns = [
    path('',  views.dashboard),
    
    path('food/busket-list', views.GetUserBasketItems),
    path('food/busket-item', views.ChangeBasketItem),
    path('food/busket-change', views.ChangeBasketItem),
    path('food/busket-clear', views.ClearUserBasket),
]