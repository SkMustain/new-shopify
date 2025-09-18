from django.core.management.base import BaseCommand

from core.models import Subject


DEFAULT_SUBJECTS = [
    "Mathematics",
    "English",
    "Physics",
    "Chemistry",
    "Biology",
    "Computer Science",
    "History",
    "Geography",
]


class Command(BaseCommand):
    help = "Seed initial subjects"

    def handle(self, *args, **options):
        created_count = 0
        for name in DEFAULT_SUBJECTS:
            subject, created = Subject.objects.get_or_create(name=name)
            if created:
                created_count += 1
        self.stdout.write(self.style.SUCCESS(f"Seeded subjects. Created: {created_count}"))
