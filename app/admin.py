
# import your admin models here.
from django.contrib import admin

from .models import *

class TrackAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'create_at', 'slug')

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'nickname', 'phone','password2', 'create_at', 'slug')

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'picture', 'create_at', 'slug')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'picture', 'create_at', 'slug')
    
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_at', 'slug')

class DateAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_at', 'slug')
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'create_at', 'slug')

class WalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'total', 'create_at', 'slug')
    
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'create_at', 'slug')

class FriendsAdmin(admin.ModelAdmin):
    list_display = ('friend', 'friendof', 'create_at', 'slug')
    
admin.site.register(Track, TrackAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Config)
admin.site.register(Task)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Date, DateAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Payment)
admin.site.register(Boucher)
admin.site.register(Cart)
admin.site.register(Buyment)
admin.site.register(Wallet, WalletAdmin)
admin.site.register(Link)
admin.site.register(Owner, OwnerAdmin)
admin.site.register(Friends, FriendsAdmin)