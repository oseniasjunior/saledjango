from rest_framework import serializers


class TotalEmployeeByDepartmentSeralizer(serializers.Serializer):
    department = serializers.CharField(read_only=True, source='name')
    counter = serializers.IntegerField(read_only=True)
