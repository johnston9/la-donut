"""Models for the Profiles App
"""
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    Connected to User model and containing user address which
    is used as a default delivery address and user order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    primary_full_name = models.CharField(max_length=50, default="", blank=True)
    primary_phone_number = models.CharField(max_length=20, default="",
                                            blank=True)
    primary_street_address1 = models.CharField(max_length=80, default="",
                                               blank=True)
    primary_street_address2 = models.CharField(max_length=80, default="",
                                               blank=True)
    primary_town_or_city = models.CharField(max_length=40, default="",
                                            blank=True)
    primary_postcode = models.CharField(max_length=20, default="", blank=True)
    primary_county = models.CharField(max_length=80, default="", blank=True)
    primary_country = CountryField(blank_label='Country', default="",
                                   blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: save the profile
    instance.userprofile.save()
