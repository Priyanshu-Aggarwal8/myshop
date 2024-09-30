from django.contrib import admin
from .models import Product, Brand, Address, Category, Feedback, CartItem
# Register your models here.
class productAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)
    list_display = ("title", "id", "isBestseller")
    list_filter = ("isBestseller",)
    search_fields = ("title", "category", "brand")

admin.site.register(Category)
admin.site.register(Product, productAdmin)
admin.site.register(Brand)
admin.site.register(Address)
admin.site.register(Feedback)
admin.site.register(CartItem)