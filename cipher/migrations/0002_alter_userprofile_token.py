# Generated by Django 5.0.1 on 2024-10-19 11:20

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cipher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='token',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
