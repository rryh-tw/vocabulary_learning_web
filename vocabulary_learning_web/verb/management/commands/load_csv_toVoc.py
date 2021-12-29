import csv
from django.core.management import BaseCommand
from django.utils import timezone

from verb.models import Vocabulary

class Command(BaseCommand):
    help = "Loads products and product categories from CSV file."

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str)

    def handle(self, *args, **options):
        start_time = timezone.now()
        file_path = options["file_path"]
        with open(file_path, "r") as csv_file:
            data = csv.reader(csv_file, delimiter=",")
            vocabularies = []
            for row in data:
                vocabulary = Vocabulary(word=row[0], translation=row[1])
                vocabularies.append(vocabulary)
            if vocabularies:
                Vocabulary.objects.bulk_create(vocabularies)
        end_time = timezone.now()
        self.stdout.write(
            self.style.SUCCESS(
                f"Loading CSV took: {(end_time-start_time).total_seconds()} seconds."
            )
        )
