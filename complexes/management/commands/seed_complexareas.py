import random
from django.core.management import BaseCommand
from django_seed import Seed
from complexes import models


class Command(BaseCommand):

    help = "단지 면적을 생성해주는 명령어입니다."

    def add_arguments(self, parser):
        parser.add_argument("--number", default=3, type=int, help="생성할 단지 면적 개수")

    def handle(self, *args, **options):
        number = options.get("number", 1)
        seeder = Seed.seeder()
        complex = models.Complex.objects.all()
        seeder.add_entity(
            models.ComplexArea,
            number,
            {
                "complex": lambda x: random.choice(complex),
                "supply_area": lambda x: random.uniform(50, 150),
                "exclusive_private_area": lambda x: random.uniform(50, 150),
                "room": lambda x: random.randint(1, 8),
                "bath": lambda x: random.randint(1, 4),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS("단지 면적이 생성되었습니다."))
