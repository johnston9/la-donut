"""Models for the Product App
"""
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Avg
from profiles.models import UserProfile


class Category(models.Model):
    """Category Model for the Product App
    """

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, default="", blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        """get_friendly_name for the Category Model
        """
        return self.friendly_name


class Product(models.Model):
    """Product Model for the Product App
    """
    class Meta:
        ordering = ['name']

    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(max_length=254, default="", blank=False)
    flavour = models.CharField(max_length=254, default="", blank=True)
    description = models.TextField()
    shop_price = models.DecimalField(max_digits=6, decimal_places=2,
                                     null=True, blank=True)
    web_price = models.DecimalField(max_digits=6, decimal_places=2,
                                    null=False, blank=False, default=0)
    is_for_six = models.BooleanField(default=False, null=True, blank=True)
    is_sizes = models.BooleanField(default=False, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, default="", blank=True)
    image = models.ImageField(null=True, blank=True)
    storage = models.CharField(max_length=254, default="", blank=True)
    is_vegan = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name

    def avg_rating(self):
        """Get average rating for each product
        """
        return Review.objects.filter(product__id=self.id).aggregate(
            Avg('rating'))['rating__avg']


class Size(models.Model):
    """Size Model for the Product App
    """
    name = models.CharField(max_length=254)
    product = models.ForeignKey('Product', null=True, blank=True,
                                on_delete=models.CASCADE, related_name='sizes')
    small = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                blank=True, default=0)
    medium = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True, default=0)
    large = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                blank=True, default=0)

    def __str__(self):
        return self.product.name


class Forsix(models.Model):
    """Forsix Model for the Product App
    """
    name = models.CharField(max_length=254)
    product = models.ForeignKey('Product', null=True, blank=True,
                                on_delete=models.CASCADE,
                                related_name='forsix')
    for6 = models.DecimalField(max_digits=6, decimal_places=2,
                               null=True, blank=True, default=0)
    for12 = models.DecimalField(max_digits=6, decimal_places=2,
                                null=True, blank=True, default=0)
    for24 = models.DecimalField(max_digits=6, decimal_places=2,
                                null=True, blank=True, default=0)

    def __str__(self):
        return self.product.name


class Review(models.Model):
    """Review Model for the Product App
    """
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    name = models.CharField(max_length=254)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True)
    product = models.ForeignKey('Product', null=True, blank=True,
                                on_delete=models.CASCADE,
                                related_name='reviews')
    review = models.TextField(max_length=1500)
    rating = models.IntegerField(choices=RATING_CHOICES, default="1")
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


@receiver(post_save, sender=Product)
def create_size_and_forsix(sender, instance, created, **kwargs):
    """
    Create size object for Product
    """
    if created:
        size = Size.objects.create(name=instance.name, product=instance)
        forsix = Forsix.objects.create(name=instance.name, product=instance)

        size.save()
        forsix.save()
