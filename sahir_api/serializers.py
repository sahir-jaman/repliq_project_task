from rest_framework import serializers
from sahir_api.models import Company, Employee, EmployeeProducts


# serializer class written here
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()

    class Meta:
        model = Company
        fields = '__all__'


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = EmployeeProducts
        fields = '__all__'
