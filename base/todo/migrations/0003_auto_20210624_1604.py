# Generated by Django 2.2.12 on 2021-06-24 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_task_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
