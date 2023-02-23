
# Register your models here.
from .models import Cart,CartItem
from django.contrib import admin

admin.site.register(Cart)
admin.site.register(CartItem)