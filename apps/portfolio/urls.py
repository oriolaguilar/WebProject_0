from django.urls import path
from apps.portfolio import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]