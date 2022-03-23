from django.db.models import Q
from django_filters import filterset

from core import models


class DepartmentFilter(filterset.FilterSet):
    name = filterset.CharFilter(lookup_expr='icontains')

    class Meta:
        model = models.Department
        fields = ['name']


class EmployeeFilter(filterset.FilterSet):
    name_or_department = filterset.CharFilter(method='filter_name_or_department')
    start_salary = filterset.CharFilter(field_name='salary', lookup_expr='gte')
    end_salary = filterset.CharFilter(field_name='salary', lookup_expr='lte')

    def filter_name_or_department(self, queryset, name, value):
        return queryset.select_related(
            'department'
        ).filter(Q(name__icontains=value) | Q(department__name__icontains=value))

    class Meta:
        model = models.Employee
        fields = ['start_salary', 'end_salary']
