from django.urls import path
from .views import get_delete_update_puppy, get_post_puppies


urlpatterns = [
    path(
        'api/v1/puppies/<int:pk>',
        get_delete_update_puppy,
        name='get_delete_update_puppy'
    ),
    path(
        'api/v1/puppies/',
        get_post_puppies,
        name='get_post_puppies'
    )
]
