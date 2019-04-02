from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User,AmazonItem,Item,ItemPurchaseHistory
# Register your models here.
admin.site.register(User,UserAdmin)
admin.site.register(AmazonItem)
admin.site.register(Item)
admin.site.register(ItemPurchaseHistory)  