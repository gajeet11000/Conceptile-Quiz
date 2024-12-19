import uuid
from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=50)
    option2 = models.CharField(max_length=50)
    option3 = models.CharField(max_length=50)
    option4 = models.CharField(max_length=50)
    def __str__(self):
        return self.question
    
class QuizSession(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    no_of_questions = models.PositiveIntegerField(default=0)
    questions = models.ManyToManyField(Question, blank=True)
    result = models.JSONField(null=True, blank=True)