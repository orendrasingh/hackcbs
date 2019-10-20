from django.urls import path

from . import views
from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('log', views.log, name='index'),
path('signup', views.signup, name='index'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)