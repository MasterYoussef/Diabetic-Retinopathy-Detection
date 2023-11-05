
from django.contrib import admin
from django.urls import path
from diab_retina_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.display),
    path('api/', views.process_image)
]
