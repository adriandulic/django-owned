from django.db import models
from django.contrib.auth.models import User
from owned.managers import OwnedManager

class Owned(models.Model):
    """
    Abstract Owned model
    """
    owner = models.ForeignKey(User)
    objects = OwnedManager()
    
    class Meta:
        abstract = True
