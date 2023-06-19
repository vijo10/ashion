from django.urls import path
from .views import shop,product_detail,search,submit_review

urlpatterns=[
  path('',shop,name='shop'),
  path('products/<slug:category_slug>/',shop,name='products_by_category'),
  path('product/<slug:category_slug>/<slug:product_slug>/',product_detail,name='product_detail'),
  path('search/',search,name='search'),
  path('submit_review/<int:product_id>/',submit_review,name='submit_review'),
]