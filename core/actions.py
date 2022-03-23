from core import models


class DepartmentActions:
    @staticmethod
    def readjustments_salary(department: 'models.Department', percentage):
        for employee in department.employee_set.all():
            employee.salary += employee.salary * (percentage / 100)
            employee.save()


class StateActions:
    @staticmethod
    def save_log_file(state: 'models.State'):
        with open('states.txt', 'a') as file:
            file.write(f'{state.name}\n')
