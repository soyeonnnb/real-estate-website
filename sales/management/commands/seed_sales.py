from django.core.management import BaseCommand
from datetime import datetime, timedelta
from django_seed import Seed
from faker import Faker
from sales import models
from django.contrib.admin.utils import flatten
from complexes import models as complexes_models
import random


class Command(BaseCommand):

    help = "매물을 생성합니다"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="몇 개의 매물을 생성할 것인지 입력해주세요."
        )

    def handle(self, *args, **options):
        number = options.get("number", 1)
        seeder = Seed.seeder()
        complex_sub = complexes_models.ComplexSub.objects.all()
        fake = Faker("ko_KR")
        seeder.add_entity(
            models.Sale,
            number,
            {
                "complex_sub": lambda x: random.choice(complex_sub),
                "address": lambda x: fake.address(),
                "deposit": lambda x: random.randint(1000, 10000000),
                "amount": lambda x: random.randint(1000000, 400000000),
                "floor": lambda x: random.randint(1, 20),
                "loan": lambda x: random.randint(0, 100000000),
                "administrative_expense": lambda x: random.randint(10000, 200000),
                "available_date": lambda x: datetime.now()
                + timedelta(days=random.randint(60, 120)),
                "description": lambda x: fake.sentence(),
                "one_description": lambda x: fake.sentence(),
            },
        )
        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))
        for pk in created_clean:
            sale = models.Sale.objects.get(pk=pk)
            for i in range(3, random.randint(6, 34)):
                models.SaleImage.objects.create(
                    description=seeder.faker.sentence(),
                    sale=sale,
                    image=f"photos/sale_photos/{random.randint(1, 34)}.jpg",
                )
        self.stdout.write(self.style.SUCCESS(f"{number}개의 매물 생성 완료"))
