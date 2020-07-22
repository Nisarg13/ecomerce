"""ecomerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('rab_shop_left_sidebar_grid/', views.rab_shop_left_sidebar_grid, name='rab_shop_left_sidebar_grid'),
    path('filter/', views.filter, name='filter'),
    path('classic/', views.classic, name='classic'),
    path('view-cart/', views.view_cart, name='view-cart'),
    path('add-cart/<int:pk>', views.add_cart, name='add-cart'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('add-wishlist/<int:pk>', views.add_wishlist, name='add-wishlist'),
    path('remove-item/<int:pk>', views.remove_item, name='remove-item'),
    path('remove_item_and_add/<int:pk>', views.remove_item_and_add, name='remove_item_and_add'),
    path('register', views.register, name='register'),
    path('registrationpage', views.registrationpage, name='registrationpage'),
    path('loginpage', views.loginpage, name='loginpage'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('remove-item-cart/<int:pk>', views.remove_item_cart, name='remove-item-cart'),
    path('incrment-product/<int:pk>', views.incrment_product, name='incrment-product'),
    path('decrment-product/<int:pk>', views.decrment_product, name='decrment-product'),
    path('checkout-view/', views.checkout_view, name='checkout-view'),
    path('order-complete/', views.order_complete, name='order-complete'),
    path('order-complete-view/', views.order_complete_view, name='order-complete-view'),
]