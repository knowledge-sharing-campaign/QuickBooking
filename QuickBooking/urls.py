from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^results/details', views.details, name='details'),
    url(r'^results', views.results, name='results'),
    url(r'^', views.index, name='index')
]
