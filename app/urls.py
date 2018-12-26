from django.conf.urls import url
from .views import *

urlpatterns = [
    #url(r'^', index, name='index'),
    url(r'^registrar/', registrar, name='registrar_usuario'),
    url(r'^registrado/', registrado, name='usuario_registrado'),
    url(r'', index, name='index'),
]