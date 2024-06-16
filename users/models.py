from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Create your models here.

class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        if not password:
            raise ValueError('Password is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    alias = models.CharField(max_length=30, unique=True, blank=True, null=True, default=None)
    phone_number = models.CharField(max_length=20, blank=True, null=True, default=None)
    first_name = models.CharField(max_length=100, blank=True, null=True, default=None)
    last_name = models.CharField(max_length=100, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_notification_required = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def update(self, instance, validated_data):
        instance.alias = validated_data.get('alias')
        instance.phone_number = validated_data.get('phone_number')
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.save()
        return instance

    def has_premium(self):
        from premium.models import UserSubscription

        user_sub = UserSubscription.objects.filter(user=self.id)
        is_active = user_sub.filter(is_active=True)
        if not is_active:
            return False
        return True

    def __str__(self):
        return self.email
