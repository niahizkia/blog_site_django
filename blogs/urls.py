from . import views
from django.urls import path
from django.conf.urls import handler404, handler500

app_name = 'blogs'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.single, name='single'),
    path('comment/<int:id>', views.comment, name='comment'),
]

hander404 = 'views.handler404'