# Generated by Django 4.2.1 on 2023-05-29 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sahir_api', '0002_remove_employeeproducts_employee_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeproducts',
            name='Employee_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sahir_api.employee'),
        ),
    ]