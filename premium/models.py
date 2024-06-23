from django.db import models
from users.models import CustomUser
from datetime import datetime, timedelta


subscription_period = (
    ('mn', 'monthly'),
    ('qt', 'quaterly'),
    ('hf', 'half_yearly'),
    ('yr', 'anually')
)


class ServiceProduct(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return self.name


class UserSubscription(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    service_chosen = models.ForeignKey(ServiceProduct, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=False)
    subscribed_on = models.DateTimeField(null=True)
    expiring_on = models.DateTimeField(null=True)
    subscription_period = models.CharField(max_length=255, choices=subscription_period, blank=False)

    def __str__(self):
        return f'{self.user}, {self.is_active}, {self.expiring_on}'

