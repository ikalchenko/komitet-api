from django.contrib.auth.models import User
from django.db import models

from users.models import UserPermissions
from .managers import KomitetManager


class Komitet(models.Model):
    members = models.ManyToManyField(User, through=UserPermissions)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    background = models.ImageField(null=True, blank=True)
    access_code = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = KomitetManager()c

    def get_not_banned(self):
        return self.members.exclude(userpermissions__permission='B')
