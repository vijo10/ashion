from django.shortcuts import render,get_object_or_404,redirect
from .models import Product,RatingReview,PhotoGallary
from category.models import Category
from cart.models import CartItem
from cart.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from .forms import ReviewForm
from django.contrib import messages
from order.models import OrderProduct

# Create your views here.
def shop(request,category_slug=None):
  categories=None
  products=None
  if category_slug != None:
    categories=get_object_or_404(Category, slug=category_slug)
    products=Product.objects.filter(category=categories, is_available=True).order_by('id')
    paginator=Paginator(products, 3)
    page=request.GET.get('page')
    paged_product=paginator.get_page(page)
    product_count=products.count()
  else:    
    products=Product.objects.all().filter(is_available=True).order_by('id')
    paginator=Paginator(products, 6)
    page=request.GET.get('page')
    paged_product=paginator.get_page(page)
    product_count=products.count()
  context={
    'products':paged_product,
    'categories':categories,
    'product_count':product_count,
  }
  return render(request,'shop/shop.html',context)

def product_detail(request,category_slug,product_slug):
  try:
    product=Product.objects.get(category__slug=category_slug,slug=product_slug)
  except Exception as e:
    raise e

  if request.user.is_authenticated:
    try:
      orderproduct =OrderProduct.objects.filter(user=request.user,product_id=product.id).exists()
    except OrderProduct.DoesNotExist:
      orderproduct=None 
  else:
     orderproduct=None
     
  reviews =RatingReview.objects.filter(product_id=product.id,status=True)   
  photo_gallary=PhotoGallary.objects.filter(product_id=product.id)
  context={
    'product':product,
    'orderproduct':orderproduct,
    'reviews':reviews,
    'photo_gallary':photo_gallary,
  }    
  return render(request,'shop/product_detail.html',context)  

def search(request):
  if 'keyword' in request.GET:
    keyword=request.GET['keyword']
    products=Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
    product_count=products.count()
  context={
    'products':products,
    'product_count':product_count,
  }
  return render(request,'shop/shop.html',context)

def submit_review(request,product_id):
  url=request.META.get('HTTP_REFERER')
  if request.method  == "POST":
    try:
      reviews=RatingReview.objects.get(user__id=request.user.id,product__id=product_id)
      form=ReviewForm(request.POST,instance=reviews)
      form.save()
      messages.success(request,'Thank you! Your review has been updated')
      return redirect(url)
    except RatingReview.DoesNotExist:
      form = ReviewForm(request.POST)
      if form.is_valid():
        data=RatingReview()
        data.subject=form.cleaned_data['subject']
        data.review=form.cleaned_data['review']
        data.rating=form.cleaned_data['rating']
        data.ip=request.META.get('REMOTE_ADDR')
        data.product_id=product_id
        data.user_id=request.user.id
        data.save()
        messages.success(request,'Thank you! Your review has been submited')
        return redirect(url)
