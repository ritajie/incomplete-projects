from typing import Any, List

from django.urls import path
from incomplete_projects.api import building

urlpatterns: List[Any] = [
    path("buildings", building.BulidingView.as_view(http_method_names=["get"])),
]
