# Generated by Django 4.2.1 on 2023-05-29 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sahir_api', '0003_employeeproducts_employee_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeeproducts',
            old_name='Employee_id',
            new_name='Employee_name',
        ),
    ]
