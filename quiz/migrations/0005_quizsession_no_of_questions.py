# Generated by Django 5.1.4 on 2024-12-18 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_rename_answer_question_option4'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizsession',
            name='no_of_questions',
            field=models.PositiveIntegerField(default=0),
        ),
    ]