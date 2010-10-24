from django.db import models
from django.conf import settings

class OwnedManager(models.Manager):
    """
    Owned manager
    """
    def owned_by(self, user=None):
        kwargs = {settings.OWNED_FIELD_NAME: user}
        return super(OwnedManager, self).get_query_set().filter(**kwargs)
