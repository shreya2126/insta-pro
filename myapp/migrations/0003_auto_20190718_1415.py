# Generated by Django 2.2.3 on 2019-07-18 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_employees_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employees',
            name='id',
        ),
        migrations.AlterField(
            model_name='employees',
            name='empid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
