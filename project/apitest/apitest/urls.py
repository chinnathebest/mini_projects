from django.contrib import admin
from django.urls import path, include
from .views import tesview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/',include('rest_framework.urls')),
    path('', tesview.as_view(),name='test')
]
