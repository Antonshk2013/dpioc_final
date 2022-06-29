from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('rosetta/', include('rosetta.urls')),
    ]

urlpatterns += i18n_patterns(
    path('', include('landing.urls')),
    path('admin/', admin.site.urls),
    prefix_default_language=False
)
handler404 = 'landing.views.handler404'
