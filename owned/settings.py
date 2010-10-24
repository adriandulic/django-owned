from django.conf import settings

# default model field name for owner
OWNED_FIELD_NAME = getattr(settings, 'OWNED_FIELD_NAME', 'owner')
