# Generated by Django 5.0.1 on 2024-10-19 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cipher', '0005_text_original_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='is_manually_added',
            field=models.BooleanField(default=True),
        ),
    ]
