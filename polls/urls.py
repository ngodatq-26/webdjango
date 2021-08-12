from django.conf.urls import url

from . import views
from polls.views import index

urlpatterns = [ 
     url(r'^$', views.index, name='index'),
]