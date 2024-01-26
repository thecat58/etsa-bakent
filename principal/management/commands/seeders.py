# principal/management/commands/seeders.py
from django.core.management.base import BaseCommand
from django_seed import Seed
from principal.models import Departamento, Municipio

class Command(BaseCommand):
    help = 'Seed the database with specific data'

    def handle(self, *args, **options):
        seeder = Seed.seeder()

        # Seed para Departamento
        departamento_data = [
            {'nombre': 'Antioquia', 'codigo': '5'},
            {'nombre': 'Atlantico', 'codigo': '8'},
            # Agrega más departamentos según sea necesario
        ]

        for data in departamento_data:
            seeder.add_entity(Departamento, 1, {
                'nombre': data['nombre'],
                'codigo': data['codigo'],
            })

        # Ejecutar el seeder para Departamento y obtener los ID insertados
        inserted_departamento_pks = seeder.execute()

        # Seed para Municipio
        municipio_data = [
            {'nombre': 'Municipio 1', 'departamento_id': Departamento.objects.get(id=inserted_departamento_pks[Departamento][0])},
            {'nombre': 'Municipio 2', 'departamento_id': Departamento.objects.get(id=inserted_departamento_pks[Departamento][1])},
            # Agrega más municipios según sea necesario
        ]

        for data in municipio_data:
            seeder.add_entity(Municipio, 1, {
                'nombre': data['nombre'],
                'departamento_id': data['departamento_id'],
            })

        # Ejecutar el seeder para Municipio y obtener los ID insertados
        inserted_municipio_pks = seeder.execute()

        # Mensajes de éxito
        self.stdout.write(self.style.SUCCESS(f'Successfully seeded Departamento data. Inserted PKs: {inserted_departamento_pks}'))
        self.stdout.write(self.style.SUCCESS(f'Successfully seeded Municipio data. Inserted PKs: {inserted_municipio_pks}'))
