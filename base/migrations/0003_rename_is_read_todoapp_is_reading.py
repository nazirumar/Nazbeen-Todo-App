# Generated by Django 4.1.1 on 2022-10-31 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_is_active_todoapp_is_read'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todoapp',
            old_name='is_read',
            new_name='is_reading',
        ),
    ]