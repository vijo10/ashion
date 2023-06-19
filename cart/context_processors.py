from .models import Cart,CartItem
from .views import _cart_id

def counter(request):
  cart_count=0
  total=0
  tax=0
  grand_total=0
  if 'admin' in request.path:
    return {}
  else:
    try:
      cart=Cart.objects.filter(cart_id=_cart_id(request)) 
      if request.user.is_authenticated:
         cart_items=CartItem.objects.filter(user=request.user) 
      else:   
        cart_items=CartItem.objects.filter(cart=cart[:1]) 
      for cart_item in cart_items:
        cart_count += cart_item.quantity
        total += cart_item.product.price * cart_item.quantity
      tax=(2*total)/100 
      grand_total= total+tax 
    except:
      cart_count=0
      total=0
  return dict(cart_count=cart_count,grand_total=grand_total)        
