import os
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)  


def UserImages(instance, filename):
    return '/'.join( ['images', 'Users', str(instance.id), filename] )

def InfluencerImages(instance, filename):
    return '/'.join( ['images', 'Influencers', str(instance.id), filename] )

class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, username, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, username, first_name, password, **other_fields)

    def create_user(self, email, username, first_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_(
        'about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    img = models.ImageField(upload_to=UserImages, default='/media/images/Users/None/index.png')
    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name']

    def __str__(self):
        return self.username

class Influencer(models.Model):

    # Data coming from Instagram
    name = models.CharField(max_length=150, blank=True)
    username = models.CharField(max_length=30, blank=True)
    about = models.TextField(max_length=150, blank=True, null=True)


    # Data fed by the influencer themselves
    services_cost = models.IntegerField(blank=True, null=True)
    children = models.ManyToManyField('Children', blank=True, related_name="children")
    img = models.ImageField(upload_to=InfluencerImages, default='media/images/Users/None/index.jpg')



class Children(models.Model):
    
    sex_choices = (
        ("Male", "M"),
        ("Female", "F"),
    )

    age = models.IntegerField(blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True, null=True)