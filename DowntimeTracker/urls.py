from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/<name>', views.dashboard, name='dashboard')
]