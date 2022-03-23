from django.db.models import Prefetch
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from core import models, serializers, serializers_params, serializers_results, actions, filters, tasks


class StateViewSet(viewsets.ModelViewSet):
    queryset = models.State.objects.all()
    serializer_class = serializers.StateSerializer

    def create(self, request, *args, **kwargs):
        result = super(StateViewSet, self).create(request, *args, **kwargs)
        state_id = result.data.get('id')
        tasks.save_log_file.apply_async([state_id])
        return result


class ZoneViewSet(viewsets.ModelViewSet):
    queryset = models.Zone.objects.all()
    serializer_class = serializers.ZoneSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    filter_class = filters.EmployeeFilter


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = models.Department.objects.prefetch_related(
        Prefetch('employee_set', queryset=models.Employee.objects.order_by('-salary'))
    ).all()
    serializer_class = serializers.DepartmentSerializer
    filter_class = filters.DepartmentFilter
    ordering_fields = '__all__'
    ordering = ('-id',)

    @action(detail=False, methods=['GET'])
    def total_employees(self, request, *args, **kwargs):
        queryset = models.Department.objects.total_employees()
        result = serializers_results.TotalEmployeeByDepartmentSeralizer(
            instance=queryset,
            context=self.get_serializer_context(),
            many=True
        )
        return Response(data=result.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['PATCH'])
    def readjustments_salary(self, request, *args, **kwargs):
        result = serializers_params.ReadjustmetnsSalarySeralizer(data=request.data, context={'request': request})
        result.is_valid(raise_exception=True)
        actions.DepartmentActions.readjustments_salary(
            department=self.get_object(),
            percentage=result.validated_data.get('percentage_readjustments')
        )
        result = self.get_serializer(instance=self.get_object(), context=self.get_serializer_context())
        return Response(data=result.data, status=status.HTTP_200_OK)


class BranchViewSet(viewsets.ModelViewSet):
    queryset = models.Branch.objects.select_related('district').all()
    serializer_class = serializers.BranchSerializer
