import random
from datetime import datetime, timedelta

from django.contrib.admin.utils import flatten
from django.core.management import BaseCommand
from django_seed import Seed
from faker import Faker

from complexes import models


class Command(BaseCommand):

    help = "이 명령어는 단지를 생성합니다."

    def add_arguments(self, parser):
        parser.add_argument("--number", default=3, type=int, help="몇 개의 단지를 생성할 것인가요")

    def handle(self, *args, **options):
        number = options.get("number", 1)
        seeder = Seed.seeder()
        categories = models.Category.objects.all()
        fake = Faker("ko_KR")
        seeder.add_entity(
            models.Complex,
            number,
            {
                "category": lambda x: random.choice(categories),
                "name": lambda x: fake.company(),
                "parking": lambda x: random.randint(100, 300),
                "company": lambda x: seeder.faker.company(),
                "latitude": lambda x: random.uniform(36.2656, 36.2891),
                "longitude": lambda x: random.uniform(127.2364, 127.2629),
                "approval_use": lambda x: datetime.now()
                - timedelta(days=random.randint(365, 1000)),
            },
        )
        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))
        for pk in created_clean:
            complex = models.Complex.objects.get(pk=pk)
            for i in range(2, random.randint(5, 10)):
                models.ComplexImage.objects.create(
                    description=seeder.faker.sentence(),
                    complex=complex,
                    image=f"photos/complexes_photos/{random.randint(1, 16)}.jpg",
                )

        self.stdout.write(self.style.SUCCESS(f"{number}개의 단지 생성이 완료되었습니다."))
