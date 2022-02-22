from django.urls import path
from locationapp.views import location
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', location),
   
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

