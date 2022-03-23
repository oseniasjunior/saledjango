from core import models
from django.db.models import Case, When, CharField, Value


def teste():
    gender_description = Case(
        When(gender='F', then=Value('Female')), default=Value('Male'),
        output_field=CharField()
    )
    return models.Employee.objects.annotate(gender_description=gender_description)
