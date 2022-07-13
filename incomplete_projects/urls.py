from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path("api/", include("incomplete_projects.api.urls")),
    path("", include("incomplete_projects.views.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
