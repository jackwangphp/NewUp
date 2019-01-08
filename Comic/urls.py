from django.urls import path

from . import views

app_name = 'Comic'
urlpatterns = [
    path('', views.index, name='index'),
]
