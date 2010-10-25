from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class OwnedManager(models.Manager):
    """
    Owned manager
    """
    def owned_by(self, user=None):
        queryset = super(OwnedManager, self).get_query_set()
        if not isinstance(user, User):
            return queryset.none()
        return queryset.filter(**{settings.OWNED_FIELD_NAME: user})
