from django.urls import path
from . import views

urlpatterns = [
    path('create-media', views.createMedia, name='createMedia'),
    path('postMedia', views.postMedia, name='postMedia'),
]
