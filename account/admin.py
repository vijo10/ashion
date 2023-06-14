from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account,UserProfile,Otp
from django.utils.html import format_html
# Register your models here.
class AccountAdmin(UserAdmin):
  list_display=('email','first_name','last_name','username','last_login','date_joined','is_active')
  list_display_links=('email','first_name','last_name')
  readonly_fileds=('last_login','date_joined')
  ordering=('-date_joined',)
  filter_horizontal=()
  list_filter=()
  fieldsets=()

admin.site.register(Account,AccountAdmin)

class UserProfileAdmin(admin.ModelAdmin):
  def thumbnail(self,object):
    return format_html(f"<img src='{object.profile_pic.url}' width='30' style='border-radius:50%;'>")
  thumbnail.short_discription="Profile Picture"
  list_display=('thumbnail','user','city','state','country')

admin.site.register(UserProfile, UserProfileAdmin)    

admin.site.register(Otp)