# Generated by Django 3.2 on 2023-11-30 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='normal_user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='normal_user',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='normal_user',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='normal_user',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='normal_user',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='normal_user',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='normal_user',
            name='password',
        ),
    ]
