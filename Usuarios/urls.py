from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.UsuariosList.as_view(),name='lista'),
#    url(r'^(?P<pk>[0-9]+)/$', views.UsuariosDetail.as_view(),name='detalle'),
#    url(r'^nuevo/$', views.UsuariosCreate.as_view(),name='nuevo'),
#    url(r'^editar/(?P<pk>[0-9]+)/$', views.UsuariosUpdate.as_view(),name='editar'),
#    url(r'^eliminar/(?P<pk>[0-9]+)/$', views.UsuariosDelete.as_view(),name='eliminar'),

]
