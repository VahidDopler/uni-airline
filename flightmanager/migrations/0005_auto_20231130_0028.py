# Generated by Django 3.2 on 2023-11-29 20:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flightmanager', '0004_auto_20231130_0025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='passengers',
        ),
        migrations.AddField(
            model_name='flight',
            name='passengers',
            field=models.ManyToManyField(null=True, related_name='flights', to=settings.AUTH_USER_MODEL),
        ),
    ]
