# Generated by Django 3.1.7 on 2021-03-30 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='adress',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='is_activte',
            new_name='is_active',
        ),
    ]