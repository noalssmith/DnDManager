from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('dashboard/<name>', views.dashboard, name='dashboard'),
    path('begin_activity', views.begin_activity, name='begin_activity'),
    path('populate', views.populate, name='populate')
]