from rest_framework import serializers
from sahir_api.models import Company, Employee, EmployeeProducts


# serializer class for Company written here
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()

    class Meta:
        model = Company
        fields = '__all__'

# serializer class for Employee written here
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Employee
        fields = '__all__'

# serializer class for Employee-Products written here
class EmployeeProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = EmployeeProducts
        fields = '__all__'
