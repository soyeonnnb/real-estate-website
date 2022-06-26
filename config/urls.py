from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("complexes/", include("complexes.urls", namespace="complexes")),
    path("posts/", include("posts.urls", namespace="posts")),
    path("questions/", include("questions.urls", namespace="questions")),
    path("sales/", include("sales.urls", namespace="sales")),
    path("users/", include("users.urls", namespace="users")),
    path("manage/", include("managements.urls", namespace="managements")),
    path("", include("core.urls", namespace="core")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
