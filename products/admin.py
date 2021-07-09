from django.contrib import admin
from .models import Product, Category, Size, Forsix, Review


class ReviewAdmin(admin.ModelAdmin):
    model = Review


class SizeAdmin(admin.ModelAdmin):
    model = Size
    readonly_fields = ('name', 'product')


class ForsixAdmin(admin.ModelAdmin):
    model = Forsix
    readonly_fields = ('name', 'product')


# class SizeAdminInline(admin.TabularInline):
class SizeAdminInline(admin.StackedInline):
    model = Size
    readonly_fields = ('name', 'product')


# class ForsixAdminInline(admin.TabularInline):
class ForsixAdminInline(admin.StackedInline):
    model = Forsix
    readonly_fields = ('name', 'product')


class ProductAdmin(admin.ModelAdmin):
    inlines = (SizeAdminInline, ForsixAdminInline)
    # readonly_fields = ('name', 'is_sizes', 'is_for_six')

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
admin.site.register(Size, SizeAdmin)
admin.site.register(Forsix, ForsixAdmin)
admin.site.register(Review, ReviewAdmin)
