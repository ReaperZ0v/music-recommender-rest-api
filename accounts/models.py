from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ValidationError

# Create your models here.

class AccountManager(BaseUserManager):
    def domain_validation(self, email):
        if "gmail.com" in email.split('@'):
            return True

        elif "outlook.com" in email.split("@"):
            return True 

        elif "icloud.com" in email.split("@"):
            return True 

        else:
            raise ValidationError('E-Mail Address Not Valid')

    def create_user(self, email, first_name, last_name, gender, age, password=None):
        email = self.normalize_email(email)
        self.domain_validation(email)

        account = self.model(email=email, first_name=first_name, last_name=last_name, gender=gender, age=age)
        account.set_password(password)

        account.save(using=self._db)
        return account 

    def create_superuser(self, email, first_name, last_name, gender, age, password):
        user = self.create_user(email, first_name, last_name, gender, age, password)
        user.is_staff = True    
        user.is_superuser = True 

        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    OPTIONS = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    date_joined = models.DateField(auto_now_add=True)
    gender = models.CharField(max_length=7, choices=OPTIONS)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    age = models.IntegerField()

    objects = AccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'gender', 'age']
    