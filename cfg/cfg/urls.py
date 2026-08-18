from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
]

# Маршруты с языковыми префиксами (/ru/, /en/)
urlpatterns += i18n_patterns(
    path("admin/", admin.site.urls),
    path("", include("portfolio.urls")),
    prefix_default_language=True,
)

# Раздача медиа и статики в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)