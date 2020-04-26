from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('web.urls', namespace='web')),
    path('api/', include('api.urls', namespace='api')),
    path('select2/', include('django_select2.urls')),
    path('admin/', admin.site.urls),
]
