from django.conf.urls import url, include
from django.contrib import admin
from Usuarios import views
from Cartera import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^usuarios/', include('Usuarios.urls', namespace='usuarios')),
    url(r'^carteras/', include('Cartera.urls', namespace='carteras')),
]
