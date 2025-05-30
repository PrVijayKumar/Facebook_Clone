from django.contrib import admin
from .models import Price, Product, ProductTag
# Register your models here.

class PriceAdmin(admin.StackedInline):
    model = Price

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (PriceAdmin, )

    class Meta:
        model = Product

admin.site.register(ProductTag)
admin.site.register(Price)
