from rest_framework import serializers
from core import models


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.State
        fields = '__all__'


class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Zone
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    employees = EmployeeSerializer(
        source='employee_set',
        read_only=True,
        many=True
    )

    class Meta:
        model = models.Department
        fields = '__all__'


class DistricSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.District
        fields = '__all__'


class BranchSerializer(serializers.ModelSerializer):
    expanded_district = DistricSerializer(
        source='district',
        read_only=True
    )

    class Meta:
        model = models.Branch
        fields = '__all__'

#
# class DepartmentSerializer(serializers.Serializer):
#     id = serializers.IntegerField(required=False)
#     created_at = serializers.DateTimeField(required=False)
#     modified_at = serializers.DateTimeField(required=False)
#     active = serializers.BooleanField(required=False)
#     name = serializers.CharField(required=True, max_length=64)
#
#     def validate(self, attrs):
#         if not attrs.get('name').isupper():
#             raise Exception('O NOME DO DEPATAMENTO TEM QUE SER EM MAISCULO')
#         return super(DepartmentSerializer, self).validate(attrs)
#
#     def create(self, validated_data):
#         return models.Department.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         for key, value in validated_data.items():
#             setattr(instance, key, value)
#         instance.save()
#         return instance
#
#     def to_representation(self, instance):
#         result = super(DepartmentSerializer, self).to_representation(instance)
#         result['custom_field'] = 'Olá mundo'
#         return result
