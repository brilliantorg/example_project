from django.urls import path
from example_app import views

urlpatterns = [
    path('hello-world/', views.hello_world, name='hello_world'),
]
