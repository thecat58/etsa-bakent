import os
from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db import connection

class Command(BaseCommand):
    help = 'Drop and recreate the database, then run migrations and seeders'

    def handle(self, *args, **kwargs):
        db_name = settings.DATABASES['default']['NAME']
        db_user = settings.DATABASES['default']['USER']
        db_password = settings.DATABASES['default']['PASSWORD']
        db_host = settings.DATABASES['default']['HOST'] or 'localhost'

        self.stdout.write(f'Dropping and recreating database: {db_name}')

        # Connect to the default database (usually 'mysql' or 'information_schema')
        with connection.cursor() as cursor:
            # Drop the database if it exists
            cursor.execute(f'DROP DATABASE IF EXISTS {db_name}')
            # Create the database again
            cursor.execute(f'CREATE DATABASE {db_name}')
            cursor.execute(f"USE {db_name}")  # Switch to the new database

            # Grant privileges to the user
            cursor.execute(f"GRANT ALL PRIVILEGES ON {db_name}.* TO '{db_user}'@'localhost'")
            cursor.execute(f"ALTER USER '{db_user}'@'localhost' IDENTIFIED BY '{db_password}'")

        self.stdout.write(self.style.SUCCESS('Database reset successfully'))

        # Run migrations (this will create all tables according to your migration files)
        call_command('migrate')

        # Optionally run your seeders or any other initialization tasks
        # This can be modified depending on your project structure
        call_command('seeders')

        self.stdout.write(self.style.SUCCESS('Migrations and seeders completed successfully'))
