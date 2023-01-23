from . import views
from django.urls import path
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('', views.index),
    path('<int:id>', views.single),
]

hander404 = 'views.handler404'