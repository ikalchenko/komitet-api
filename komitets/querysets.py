from django.db import models
from django.db.models import Q


class KomitetQuerySet(models.QuerySet):
    def users_komitets(self, user=None):
        if user:
            return self.filter(
                Q(members__id=user.id) & ~Q(userpermissions__permission='B')) \
                .order_by('-updated')
        return self
