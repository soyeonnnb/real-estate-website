from django.core.management import BaseCommand
from django_seed import Seed
from complexes import models
import random


class Command(BaseCommand):

    help = "아파트 별 층/위치를 나타내는 모델을 생성"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="몇 개의 동을 생성할 것인지 입력해주세요"
        )

    def handle(self, *args, **options):
        number = options.get("number", 1)
        seeder = Seed.seeder()
        complex_area = models.ComplexArea.objects.all()
        seeder.add_entity(
            models.ComplexSub,
            number,
            {
                "complex_area": lambda x: random.choice(complex_area),
                "building": lambda x: random.randint(100, 120),
                "floor": lambda x: random.randint(0, 20),
                "apartment": lambda x: random.randint(100, 200),
                "latitude": lambda x: random.uniform(36.2656, 36.2891),
                "longitude": lambda x: random.uniform(127.2364, 127.2629),
            },
        )

        seeder.execute()
        self.stdout.write(self.style.SUCCESS("단지 별 동/층 이 생성되었습니다"))
