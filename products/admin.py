"""admin for Product App
"""
from django.contrib import admin
from .models import Product, Category, Size, Forsix, Review


class ReviewAdmin(admin.ModelAdmin):
    """admin for Review model
    """
    model = Review


class SizeAdmin(admin.ModelAdmin):
    """admin for Size model
    """
    model = Size
    readonly_fields = ('name', 'product')


class ForsixAdmin(admin.ModelAdmin):
    """admin for Forsix model
    """
    model = Forsix
    readonly_fields = ('name', 'product')


# class SizeAdminInline(admin.TabularInline):
class SizeAdminInline(admin.StackedInline):
    """Inline admin for Size model
    """
    model = Size
    readonly_fields = ('name', 'product')


# class ForsixAdminInline(admin.TabularInline):
class ForsixAdminInline(admin.StackedInline):
    """Inline admin for Forsix model
    """
    model = Forsix
    readonly_fields = ('name', 'product')


class ProductAdmin(admin.ModelAdmin):
    """admin for Product model
    """
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
    """admin for Category model
    """
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Forsix, ForsixAdmin)
admin.site.register(Review, ReviewAdmin)
