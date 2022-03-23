from django.contrib import admin
from core import models


# Register your models here.
@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'modified_at', 'active']
    list_display_links = ['id', 'name', 'modified_at', 'active']
    search_fields = ['name']


@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'gender', 'modified_at', 'active']
    list_display_links = ['id', 'name', 'gender', 'modified_at', 'active']
    search_fields = ['name']
