
# import your admin models here.
from django.contrib import admin

from .models import *

class TrackAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'create_at', 'slug')

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'nickname', 'password2', 'create_at', 'slug')

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'picture', 'create_at', 'slug')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'picture', 'create_at', 'slug')
    
admin.site.register(Track, TrackAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Config)
admin.site.register(Task)
admin.site.register(Company)
admin.site.register(Date)
admin.site.register(Product)
admin.site.register(Payment)
admin.site.register(Boucher)
admin.site.register(Cart)
admin.site.register(Buyment)