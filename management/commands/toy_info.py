from django.core.management.base import BaseCommand
from ...utils import get_toy_info


class Command(BaseCommand):
    help = "Displays some toy information"

    def handle(self, *args, **options):
        info = get_toy_info()
        content = info.content.decode("utf-8")
        self.stdout.write(content)
        # for key, value in info.items():
        #     self.stdout.write(f"{key}: {value}")
