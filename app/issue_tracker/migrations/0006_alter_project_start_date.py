# Generated by Django 4.1.7 on 2023-03-10 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issue_tracker', '0005_alter_project_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(verbose_name='Дата начала'),
        ),
    ]
