from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.db import models
from random import randint

# Create your models here.


def rssts(email):
    f = list(email).index('@')
    return f'{email[:3]}*****{email[f:]}'


def generateRandom():
    fg = f'{randint(1, 9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}'
    return eval(fg)


class AccuntManager(BaseUserManager):

    def create_user(self, name, email, username, dob, password, **args):
        if not email:
            raise ValueError(_("User must have an email"))
        if not username:
            raise ValueError(_("User must have an usrename"))
        email = self.normalize_email(email)
        user = self.model(name=name,
                          email=email,
                          username=username,
                          dob=dob,
                          **args)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, name, email, username, dob, password, **args):
        args.setdefault('is_staff', True)
        args.setdefault('is_superuser', True)
        args.setdefault('is_active', True)
        if args.get("is_staff") is not True:
            raise ValueError('Is staff is not set to False')
        if args.get("is_superuser") is not True:
            raise ValueError('Is staff is not set to False')
        return self.create_user(name, email, username, dob, password, **args)


class account(AbstractUser, PermissionsMixin):
    name = models.CharField(max_length=100, null=False)
    mobile = models.CharField(max_length=11, null=False, unique=True)
    dob = models.DateField(verbose_name='birth day', null=True, blank=True)

    username = models.CharField(max_length=200, unique=True, null=False)
    email = models.EmailField(_('email address'),
                              max_length=200,
                              unique=True,
                              null=False)

    profilePic = models.ImageField(default="2023.png")
    password = models.CharField(max_length=200, null=False)
    code = models.IntegerField(default=generateRandom())
    date_joined = models.DateTimeField(verbose_name='date_joined',
                                       auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last_login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = AccuntManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name', 'dob']

    def __str__(self):
        return self.name

    def dsply(self):
        return rssts(self.email)


class temppwd(models.Model):
    "to store password temporarily"
    password = models.CharField(max_length=200, null=False)
    code = models.IntegerField(default=generateRandom())
    userId = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=200, null=True)

    def dsply(self):
        return rssts(self.email)


class tempuser(models.Model):
    "to store user info temporarily"
    name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=11)
    dob = models.DateField(null=True, blank=True)
    code = models.IntegerField(default=generateRandom())
    password = models.CharField(max_length=200, null=True)
    username = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)

    def dsply(self):
        return rssts(self.email)
