from django.db import models
from django.db.models import Count


class DepartmentManager(models.Manager):
    def total_employees(self):
        return self.get_queryset().values('name').annotate(
            counter=Count('employee__id'),
        ).values('name', 'counter')
