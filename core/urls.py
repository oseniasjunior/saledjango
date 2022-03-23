from rest_framework.routers import DefaultRouter
from core import viewsets

# http://127.0.0.1:8000/sale/core/
router = DefaultRouter()
router.register('zone', viewsets.ZoneViewSet)  # http://127.0.0.1:8000/sale/core/zone/
router.register('department', viewsets.DepartmentViewSet)  # http://127.0.0.1:8000/sale/core/department/
router.register('branch', viewsets.BranchViewSet)  # http://127.0.0.1:8000/sale/core/branch/
router.register('employee', viewsets.EmployeeViewSet)  # http://127.0.0.1:8000/sale/core/employee/
router.register('state', viewsets.StateViewSet)  # http://127.0.0.1:8000/sale/core/state/

urlpatterns = router.urls
