from django.urls import path
from .views import cart,add_cart,decrease_quantity,remove_cart_item,checkout

urlpatterns = [
    path('',cart,name='cart'),
    path('add_cart/<int:product_id>/',add_cart,name='add_cart'),
    path('decrease_quantity/<int:product_id>/<int:cart_item_id>/',decrease_quantity,name='decrease_quantity'),
    path('remove_cart_item/<int:product_id>/<int:cart_item_id>/',remove_cart_item,name='remove_cart_item'),
    path('checkout/',checkout,name='checkout'),
]
