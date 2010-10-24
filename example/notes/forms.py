from notes.models import Note
from django.forms import models

class NoteForm(models.ModelForm):
	class Meta:
		model = Note
