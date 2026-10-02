from django.contrib import admin
from .models import *
@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display=('title','store','category','price','old_price','active','votes','created_at')
    list_filter=('active','store','category')
    search_fields=('title','description','coupon')
    prepopulated_fields={'slug':('title',)}
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin): list_display=('name','slug'); prepopulated_fields={'slug':('name',)}
@admin.register(Store)
class StoreAdmin(admin.ModelAdmin): list_display=('name','verified'); prepopulated_fields={'slug':('name',)}
admin.site.register([Favorite,PriceAlert,Vote,Coupon,Newsletter,ContactMessage])
admin.site.site_header='Pechincha+ • Administração'
admin.site.site_title='Pechincha+'
