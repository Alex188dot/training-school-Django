from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index, name='corsiHome'),
    path('corso/<int:corso_id>', views.corso_singolo, name='corso_singolo'),
    path('registrazioneAlunno', views.registrazioneAlunno, name='registrazioneAlunno'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)