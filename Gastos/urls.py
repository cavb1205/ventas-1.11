from django.conf.urls import url
from .views import GastosList, GastosDetail, GastosCreation, GastosUpdate, GastosDelete

urlpatterns = [
    url(r'^$', GastosList.as_view(),name='list'),
    url(r'^(?P<pk>\d+)$', GastosDetail.as_view(),name='detail'),
    url(r'^nuevo/$', GastosCreation.as_view(),name='new'),
    url(r'^editar/(?P<pk>\d+)$', GastosUpdate.as_view(),name='edit'),
    url(r'^eliminar/(?P<pk>\d+)$', GastosDelete.as_view(),name='delete'),

]
