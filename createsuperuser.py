from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class CreateSuperuserCommand(BaseCommand):
    help = 'Creates a superuser if the database file is deleted'

    def handle(self, *args, **options):
        try:
            User.objects.all()
        except (Exception,):
            # Database file is deleted, create a superuser
            username = "admin"
            email = ""
            password = "admin"

            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write('Superuser created successfully.')
        else:
            # Database file exists, no action needed
            self.stdout.write('Database file exists, no action needed.')
