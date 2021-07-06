from django.urls import path
from . import views
urlpatterns = [
path('', views.cart_detail, name='cart-detail'),
path('add-to-cart/<int:product_id>', views.add_to_cart, name="add-to-cart")
]