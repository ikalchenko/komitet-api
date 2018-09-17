from django.db import models
from .querysets import KomitetQuerySet


class KomitetManager(models.Manager):
    def get_queryset(self):
        return KomitetQuerySet(self.model, self._db)

    def users_komitets(self, user=None):
        return self.get_queryset().users_komitets(user=user)
