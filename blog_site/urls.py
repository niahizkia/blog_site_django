from . import views
from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('blogs/', include('blogs.urls')),
    path('', views.welcome),
    path('admin/', admin.site.urls),
]


urlpatterns += staticfiles_urlpatterns()