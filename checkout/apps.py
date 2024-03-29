"""Set the Checkout App
"""
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """Set the Checkout App
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        import checkout.signals
