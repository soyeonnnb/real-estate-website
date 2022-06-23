from django.core.management import BaseCommand

from complexes.models import Category

# 이 명령어는 fake아니어도 실행
class Command(BaseCommand):

    help = "이 명령어는 카테고리를 생성합니다."

    def handle(self, *args, **options):

        categories = ["빌라", "오피스텔·도시형생활주택", "아파트", "공공주택", "상가", "사무실", "토지"]

        for c in categories:
            Category.objects.create(name=c)

        self.stdout.write(self.style.SUCCESS("카테고리 생성이 완료되었습니다."))
