from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from sahir_api.models import Company, Employee, EmployeeProducts
from .serializers import CompanySerializer, EmployeeSerializer, EmployeeProductSerializer


# creating views here
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    # companies/{companyId}/employees
    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        company = Company.objects.get(pk=pk)
        emps = Employee.objects.filter(company=company)
        emps_serializer = EmployeeSerializer(emps, many=True, context={'request': request})
        return Response(emps_serializer.data)

    # companies/{companyId}/employeeproducts
    @action(detail=True, methods=['get'])
    def employeeproducts(self, request, pk=None):
        company = Company.objects.get(pk=pk)
        products = EmployeeProducts.objects.filter(Employee_company=company)
        products_serializer = EmployeeProductSerializer(products, many=True, context={'request': request})
        return Response(products_serializer.data)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer



class EmployeeProductViewSet(viewsets.ModelViewSet):
    queryset = EmployeeProducts.objects.all()
    serializer_class = EmployeeProductSerializer


