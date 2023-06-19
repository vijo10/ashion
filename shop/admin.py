from django.contrib import admin
from .models import Product, Variation,RatingReview,PhotoGallary
import admin_thumbnails

@admin_thumbnails.thumbnail('image')
class PhotoGallaryInline(admin.TabularInline):
    model = PhotoGallary
    extra = 1

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
  list_display=('product_name','price','stock','category','modified_date','is_available')
  prepopulated_fields={'slug':('product_name',)}
  inlines = [PhotoGallaryInline]
admin.site.register(Product,ProductAdmin)

class VariationAdmin(admin.ModelAdmin):
  list_display=('product','variation_category','variation_value','is_active')
  list_editable=('is_active',)
  list_filter=('product','variation_category','variation_value')
admin.site.register(Variation,VariationAdmin)

admin.site.register(RatingReview)
