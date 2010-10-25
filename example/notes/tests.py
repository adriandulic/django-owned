__test__ = {"doctest": """
>>> from notes.models import Note
>>> from notes.forms import NoteForm
>>> from django.contrib.auth.models import User, AnonymousUser
>>> from owned.generic import *

# create some users
>>> guest = AnonymousUser()
>>> owner = User.objects.create_user("owner", "owner@example.com")

# create note object
>>> note = Note(title='Some title', content='Some content')
>>> note.owner = owner
>>> note.save()

# now get some notes
>>> Note.objects.all()
[<Note: Note object>]
>>> Note.objects.owned_by(owner)
[<Note: Note object>]
>>> Note.objects.owned_by(guest)
[]

# try some forms
>>> data = {'title': 'New title', 'content': 'New content', 'owner': owner.pk}
>>> form = NoteForm(data=data)
>>> form.save()
<Note: Note object>

# ... and check owner notes
>>> Note.objects.owned_by(owner)
[<Note: Note object>, <Note: Note object>]

>>> get_owned_object(Note, owner, pk=1).title
u'Some title'
>>> get_owned_object(Note, guest, pk=1)
Traceback (most recent call last):
...
DoesNotExist: Note matching query does not exist.

>>> [note.title for note in get_owned_list(Note, owner)]
[u'Some title', u'New title']
>>> [note.title for note in get_owned_list(Note, guest)]
[]

>>> get_owned_object_or_404(Note, owner, pk=1).title
u'Some title'
>>> get_owned_object_or_404(Note, guest)
Traceback (most recent call last):
...
Http404: No Note matches the given query.

>>> [note.title for note in get_owned_list_or_404(Note, owner)]
[u'Some title', u'New title']
>>> [note.title for note in get_owned_list_or_404(Note, guest)]
Traceback (most recent call last):
...
Http404: No Note matches the given query.
"""}

