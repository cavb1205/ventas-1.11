from django.conf.urls import url
from .views import UsuariosList, UsuariosDetail, UsuariosCreation, UsuariosUpdate, UsuariosDelete

urlpatterns = [
    url(r'^$', UsuariosList.as_view(),name='list'),
    url(r'^(?P<pk>\d+)$', UsuariosDetail.as_view(),name='detail'),
    url(r'^nuevo/$', UsuariosCreation.as_view(),name='new'),
    url(r'^editar/(?P<pk>\d+)$', UsuariosUpdate.as_view(),name='edit'),
    url(r'^eliminar/(?P<pk>\d+)$', UsuariosDelete.as_view(),name='delete'),

]
