# Generated by Django 5.1.4 on 2024-12-18 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizsession',
            name='result',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
