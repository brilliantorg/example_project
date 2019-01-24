from django.conf.urls import url
from example_app import views

urlpatterns = [
    url('^hello-world/$', views.hello_world, name='hello_world'),
]
