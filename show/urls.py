from django.conf.urls import url, patterns
from show import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
