# signals.py
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.core.management import call_command
from principal.models import Departamento  # Ajusta 'principal' al nombre de tu aplicación

@receiver(post_migrate)
def on_post_migrate(sender, **kwargs):
    if sender.name == 'principal':
        call_command('seeders')
