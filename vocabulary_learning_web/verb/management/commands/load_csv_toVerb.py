import csv
from django.core.management import BaseCommand
from django.utils import timezone

from verb.models import Verb, TenseCategory, Conjugaison

class Command(BaseCommand):
    help = "Loads products and product categories from CSV file."

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str)

    def handle(self, *args, **options):
        start_time = timezone.now()
        file_path = options["file_path"]
        with open(file_path, "r") as csv_file:
            data = csv.reader(csv_file, delimiter=",")
            conjugaisons = []
            verbs = {verb.infinitive: verb for verb in Verb.objects.all()}
            tenseCategories = {(tenseCategory.category, tenseCategory.tense): tenseCategory for tenseCategory in TenseCategory.objects.all()}

            for row in data:
                # Verb.infinitive, Verb.translation, state, Tense.tense, 
                verb = verbs.get(row[0])
                #create vs b
                if not verb:
                    verb = Verb.objects.create(infinitive=row[0], translation=row[1])
                    verbs[row[0]] = verb

                tenseCategory = tenseCategories.get((row[3], row[4]))
                if not tenseCategory:
                    tenseCategory = TenseCategory.objects.create(category=row[3], tense=row[4])
                    tenseCategories[(row[3],row[4])] = tenseCategory
                conjugaison = Conjugaison(
                    verb = verb,
                    state = row[2],
                    tense = tenseCategory,
                    je = row[5],
                    tu = row[6],
                    il = row[7],
                    nous = row[8],
                    vous = row[9],
                    ils = row[10]
                )
                conjugaisons.append(conjugaison)
            if conjugaisons:
                Conjugaison.objects.bulk_create(conjugaisons)
        end_time = timezone.now()
        self.stdout.write(
            self.style.SUCCESS(
                f"Loading CSV took: {(end_time-start_time).total_seconds()} seconds."
            )
        )