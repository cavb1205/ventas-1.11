from django.conf.urls import url
from .views import BaseList, BaseDetail, BaseCreation, BaseUpdate, BaseDelete

urlpatterns = [
    url(r'^$', BaseList.as_view(),name='list'),
    url(r'^(?P<pk>\d+)$', BaseDetail.as_view(),name='detail'),
    url(r'^nuevo/$', BaseCreation.as_view(),name='new'),
    url(r'^editar/(?P<pk>\d+)$', BaseUpdate.as_view(),name='edit'),
    url(r'^eliminar/(?P<pk>\d+)$', BaseDelete.as_view(),name='delete'),

]
