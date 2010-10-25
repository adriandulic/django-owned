from django.conf import settings
from django.views.generic import GenericViewError
from django.shortcuts import get_list_or_404, get_object_or_404
from django.views.generic.list_detail import object_list, object_detail
from django.contrib.auth.models import User

def owned_object_detail(request, *args, **kwargs):
    """
    owned django.views.generic.list_detail.object_detail
    """
    return object_detail(request, *args, **generic_filters(request, **kwargs))

def owned_object_list(request, *args, **kwargs):
    """
    owned django.views.generic.list_detail.object_list
    """
    return object_list(request, *args, **generic_filters(request, **kwargs))

def get_owned_object_or_404(cls, user=None, **kwargs):
    """
    owned django.shortcuts.get_object_or_404
    """
    return get_object_or_404(cls, **object_filters(user, **kwargs))

def get_owned_list_or_404(cls, user=None, **kwargs):
    """
    owned django.shortcuts.get_list_or_404
    """
    return get_list_or_404(cls, **object_filters(user, **kwargs))

def get_owned_object(cls, user=None, **kwargs):
    """
    owned Model.objects.get(...)
    """
    return cls._default_manager.get(**object_filters(user, **kwargs))

def get_owned_list(cls, user=None, **kwargs):
    """
    owned Model.ojects.filter(...)
    """
    return cls._default_manager.filter(**object_filters(user, **kwargs))

def object_filters(user=None, **kwargs):
    """
    Prepare kwargs to filter single object
    """
    user_pk = user.pk if isinstance(user, User) else None
    kwargs.update({settings.OWNED_FIELD_NAME: user_pk})
    return kwargs

def generic_filters(request, **kwargs):
    """
    Modify kwargs['queryset'] for generic views to filter objects
    """
    try:
        queryset = kwargs.pop('queryset')
        queryset = queryset.filter(**object_filters(request.user))
        kwargs['queryset'] = queryset
        return kwargs
    except KeyError:
        raise GenericViewError, 'Attribute "queryset" is missing'
