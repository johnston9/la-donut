from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    flavour = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    shop_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    web_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    is_for_six = models.BooleanField(default=False, null=True, blank=True)
    rating = models.DecimalField(max_digits=1, decimal_places=0, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    storage = models.CharField(max_length=254, null=True, blank=True)
    is_vegan = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name


class Price(models.Model):

    name = models.CharField(max_length=254)

    product_id = models.ForeignKey('Product', null=True, blank=True, on_delete=models.SET_NULL)
    small = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    medium = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    large = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name
