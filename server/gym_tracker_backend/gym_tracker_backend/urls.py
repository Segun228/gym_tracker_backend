from django.contrib import admin
from django.urls import path, include
from users.urls import urlpatterns as auth_urls
from api.urls import urlpatterns as api_urls
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


urlpatterns = [
    path("docs/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("docs/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("admin/", admin.site.urls),
    
    path("user/", include(auth_urls), name="Authentication-endpoint-group"),
    path("api/", include(api_urls), name="API-endpoint-group"),
]