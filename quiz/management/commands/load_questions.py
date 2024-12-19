import csv
import os
from django.core.management.base import BaseCommand
from quiz.models import Question
from django.conf import settings


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        csv_file = "quizes.csv"
        db_path = settings.DATABASES['default']['NAME']
        
        try:
            with open(csv_file, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                questions = []

                for row in reader:
                    question = Question(
                        question = row['Question'],
                        option1 = row['Option1'],
                        option2 = row['Option2'],
                        option3 = row['Option3'],
                        option4 = row['Option4'],
                    )
                    questions.append(question)
                
                Question.objects.bulk_create(questions)

            self.stdout.write(self.style.SUCCESS(f'Successfully imported questions from {csv_file}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error importing questions: {e}'))