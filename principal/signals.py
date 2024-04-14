from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.core.management import call_command
from principal.models import Departamento, SeederStatus

@receiver(post_migrate)
def on_post_migrate(sender, **kwargs):
    if sender.name == 'principal':
        seeder_status, created = SeederStatus.objects.get_or_create()
        if not seeder_status.seeds_applied:
            call_command('seeders')
            seeder_status.seeds_applied = True
            seeder_status.save()
