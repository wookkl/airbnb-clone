from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "This commans tells me that he loves me"

    def add_arguments(self, parser):
        parser.add_argument(
            "--times",
            help="How many times do you want me to tell you that i love you",
        )

    def handle(self, *args, **options):
        times = int(options.get("times"))
        for _ in range(times):
            print("I love you")
