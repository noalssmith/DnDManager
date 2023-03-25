from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('dashboard/<name>', views.dashboard, name='dashboard'),
    path('populate', views.populate, name='populate')
]