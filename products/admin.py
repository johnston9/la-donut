from django.contrib import admin
from .models import Product, Category, Size, Forsix

# Register your models here.


class SizeAdminInline(admin.TabularInline):
    model = Size


class ForsixAdminInline(admin.TabularInline):
    model = Forsix


class ProductAdmin(admin.ModelAdmin):
    inlines = (SizeAdminInline, ForsixAdminInline)

    list_display = (
        'name',
        'category',
        'web_price',
        'is_for_six',
        'is_sizes',
        'image',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Size)
admin.site.register(Forsix)
