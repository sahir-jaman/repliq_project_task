from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .views import CompanyViewSet, EmployeeViewSet, EmployeeProductViewSet

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'employeeproducts', EmployeeProductViewSet)

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include(router.urls))

]
