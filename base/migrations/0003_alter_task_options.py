# Generated by Django 5.0.6 on 2024-06-23 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_tasks_task'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['comp']},
        ),
    ]