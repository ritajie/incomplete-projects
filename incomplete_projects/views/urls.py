from django.urls import path

from .index import index

urlpatterns = [
    path("", index),
]
