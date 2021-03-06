# Generated by Django 4.0.3 on 2022-03-16 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_city_district_maritalstatus_state_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='state',
            field=models.ForeignKey(db_column='id_state', on_delete=django.db.models.deletion.DO_NOTHING, related_name='cities', to='core.state'),
        ),
    ]
