# Generated by Django 4.2.1 on 2024-02-25 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0002_alter_women_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='women',
            name='slug',
            field=models.SlugField(default=0, max_length=255, unique=True),
            preserve_default=False,
        ),
    ]