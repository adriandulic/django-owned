from django.db import models
from owned.models import Owned

class Note(Owned):
	title = models.CharField(max_length=50)
	content = models.TextField()
