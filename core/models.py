from django.db import models
from core import managers


class ModelBase(models.Model):
    id = models.AutoField(
        null=False,
        primary_key=True
    )
    created_at = models.DateTimeField(
        null=False,
        auto_now_add=True
    )
    modified_at = models.DateTimeField(
        null=False,
        auto_now=True
    )
    active = models.BooleanField(
        default=True
    )

    class Meta:
        abstract = True


# Create your models here.
class Zone(ModelBase):
    name = models.CharField(
        null=False,
        max_length=64,
        unique=True
    )

    class Meta:
        db_table = 'zone'
        managed = True


class Department(ModelBase):
    name = models.CharField(
        null=False,
        max_length=64,
        unique=True
    )

    objects = managers.DepartmentManager()

    class Meta:
        db_table = 'department'
        managed = True

    def __str__(self):
        return self.name


class MaritalStatus(ModelBase):
    name = models.CharField(
        null=False,
        max_length=64,
        unique=True
    )

    class Meta:
        db_table = 'marital_status'
        managed = True


class State(ModelBase):
    name = models.CharField(
        null=False,
        max_length=64,
        unique=True
    )
    abbreviation = models.CharField(
        null=False,
        max_length=2
    )

    class Meta:
        db_table = 'state'
        managed = True


class City(ModelBase):
    name = models.CharField(
        null=False,
        max_length=64,
    )
    state = models.ForeignKey(
        related_name='cities',
        to='State',
        on_delete=models.DO_NOTHING,
        db_column='id_state',
        null=False
    )

    class Meta:
        db_table = 'city'
        managed = True


class District(ModelBase):
    name = models.CharField(
        null=False,
        max_length=64,
    )
    zone = models.ForeignKey(
        to='Zone',
        on_delete=models.DO_NOTHING,
        db_column='id_zone',
        null=False
    )
    city = models.ForeignKey(
        to='City',
        on_delete=models.DO_NOTHING,
        db_column='id_city',
        null=False
    )

    class Meta:
        db_table = 'district'
        managed = True


class Employee(ModelBase):
    class Gender(models.TextChoices):
        MALE = ('M', 'Male')
        FEMALE = ('F', 'Female')

    name = models.CharField(
        null=False,
        max_length=64,
    )
    salary = models.DecimalField(
        null=False,
        max_digits=16,
        decimal_places=2
    )
    admission_date = models.DateField(
        null=False
    )
    birth_date = models.DateField(
        null=False
    )
    gender = models.CharField(
        null=False,
        max_length=1,
        choices=Gender.choices
    )
    department = models.ForeignKey(
        to='Department',
        on_delete=models.DO_NOTHING,
        db_column='id_department',
        null=False
    )
    marital_status = models.ForeignKey(
        to='MaritalStatus',
        on_delete=models.DO_NOTHING,
        db_column='id_marital_status',
        null=False
    )
    district = models.ForeignKey(
        to='District',
        on_delete=models.DO_NOTHING,
        db_column='id_district',
        null=False
    )

    class Meta:
        db_table = 'employee'
        managed = True

    def __str__(self):
        return self.name


class Customer(ModelBase):
    class Gender(models.TextChoices):
        MALE = ('M', 'Male')
        FEMALE = ('F', 'Female')

    name = models.CharField(
        null=False,
        max_length=64,
    )
    income = models.DecimalField(
        null=False,
        max_digits=16,
        decimal_places=2
    )
    gender = models.CharField(
        null=False,
        max_length=1,
        choices=Gender.choices
    )
    marital_status = models.ForeignKey(
        to='MaritalStatus',
        on_delete=models.DO_NOTHING,
        db_column='id_marital_status',
        null=False
    )
    district = models.ForeignKey(
        to='District',
        on_delete=models.DO_NOTHING,
        db_column='id_district',
        null=False
    )

    class Meta:
        db_table = 'customer'
        managed = True


class Branch(ModelBase):
    name = models.CharField(
        null=False,
        max_length=64,
        unique=True
    )
    district = models.ForeignKey(
        to='District',
        on_delete=models.DO_NOTHING,
        db_column='id_district',
        null=False
    )

    class Meta:
        db_table = 'branch'
        managed = True


class Supplier(ModelBase):
    name = models.CharField(
        null=False,
        max_length=64,
        unique=True
    )
    legal_document = models.CharField(
        null=False,
        max_length=20,
        unique=True
    )

    class Meta:
        db_table = 'supplier'
        managed = True


class ProductGroup(ModelBase):
    name = models.CharField(
        null=False,
        max_length=64,
        unique=True
    )
    commission_percentage = models.DecimalField(
        null=False,
        max_digits=5,
        decimal_places=2
    )
    gain_percentage = models.DecimalField(
        null=False,
        max_digits=5,
        decimal_places=2
    )

    class Meta:
        db_table = 'product_group'
        managed = True


class Product(ModelBase):
    name = models.CharField(
        null=False,
        max_length=64,
        unique=True
    )
    cost_price = models.DecimalField(
        null=False,
        max_digits=16,
        decimal_places=2
    )
    sale_price = models.DecimalField(
        null=False,
        max_digits=16,
        decimal_places=2
    )
    supplier = models.ForeignKey(
        to='Supplier',
        on_delete=models.DO_NOTHING,
        db_column='id_supplier',
        null=False
    )
    product_group = models.ForeignKey(
        to='ProductGroup',
        on_delete=models.DO_NOTHING,
        db_column='id_product_group',
        null=False
    )

    class Meta:
        db_table = 'product'
        managed = True


class Sale(ModelBase):
    date = models.DateTimeField(
        null=False,
        auto_now_add=True
    )
    branch = models.ForeignKey(
        to='Branch',
        on_delete=models.DO_NOTHING,
        db_column='id_branch',
        null=False
    )
    customer = models.ForeignKey(
        to='Customer',
        on_delete=models.DO_NOTHING,
        db_column='id_customer',
        null=False
    )
    employee = models.ForeignKey(
        to='Employee',
        on_delete=models.DO_NOTHING,
        db_column='id_employee',
        null=False
    )

    class Meta:
        db_table = 'sale'
        managed = True


class SaleItem(ModelBase):
    quantity = models.DecimalField(
        null=False,
        max_digits=16,
        decimal_places=3
    )
    sale = models.ForeignKey(
        to='Sale',
        on_delete=models.DO_NOTHING,
        db_column='id_sale',
        null=False
    )
    product = models.ForeignKey(
        to='Product',
        on_delete=models.DO_NOTHING,
        db_column='id_product',
        null=False
    )
    sale_price = models.DecimalField(
        null=False,
        max_digits=16,
        decimal_places=2,
        default=0
    )

    class Meta:
        db_table = 'sale_item'
        managed = True
