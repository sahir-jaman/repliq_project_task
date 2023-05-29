from django.contrib import admin
from django.urls import path, include
from .views import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_page),
    path('sahir_api/', include('sahir_api.urls')), # linking to the sahir_api.urls 
]
