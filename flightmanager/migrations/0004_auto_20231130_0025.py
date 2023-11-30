# Generated by Django 3.2 on 2023-11-29 20:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flightmanager', '0003_remove_country_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='airplane',
            name='flight',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='passengers',
        ),
        migrations.AddField(
            model_name='flight',
            name='passengers',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='flights', to=settings.AUTH_USER_MODEL),
        ),
    ]
