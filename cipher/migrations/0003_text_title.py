# Generated by Django 5.0.1 on 2024-10-19 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cipher', '0002_alter_userprofile_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='title',
            field=models.CharField(default='title1', max_length=200),
            preserve_default=False,
        ),
    ]
