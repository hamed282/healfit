from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    birthdate = models.DateField()

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'birthdate', 'password']

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class AddressModel(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_address')
    first_name_address = models.CharField(max_length=100)
    last_name_address = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    VAT_number = models.CharField(max_length=100)
    address = models.TextField(max_length=100)
    address_complement = models.TextField(max_length=100)
    phone_number = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    identification_number = models.CharField(max_length=100)
    # active_address = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user}'
