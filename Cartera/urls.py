from django.conf.urls import url
from .views import CarteraList, CarteraDetail, CarteraCreation, CarteraUpdate, CarteraDelete

urlpatterns = [
    url(r'^$', CarteraList.as_view(),name='list'),
    url(r'^(?P<pk>\d+)$', CarteraDetail.as_view(),name='detail'),
    url(r'^nuevo/$', CarteraCreation.as_view(),name='new'),
    url(r'^editar/(?P<pk>\d+)$', CarteraUpdate.as_view(),name='edit'),
    url(r'^eliminar/(?P<pk>\d+)$', CarteraDelete.as_view(),name='delete'),

]
