from django.urls import path
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('', Home.as_view(), name="index"),
    path('contacto.html', contacto, name="contacto"),
    path('about.html', about, name='about'),
    path('post/<slug:url>/', Vistaposteo.as_view(), name='post'),
    path('remodelaciones.html', Remodelaciones.as_view(), name='remodelaciones'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
