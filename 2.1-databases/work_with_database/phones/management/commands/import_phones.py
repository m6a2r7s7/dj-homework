import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('import_phones',
                            action='store_true')


    def handle(self, *args, **options):
        if options['import_phones']:
            with open('phones.csv', 'r') as file:
                phones = list(csv.DictReader(file, delimiter=';'))
            for phone in phones:
                # TODO: Добавьте сохранение модели
                res = Phone(id=phone['id'],
                            name=phone['name'],
                            price=phone['price'],
                            image=phone['image'],
                            release_date=phone['release_date'],
                            lte_exists=phone['lte_exists'])
                res.save()
            print('успешно!')
