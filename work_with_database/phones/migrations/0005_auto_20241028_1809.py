# Generated by Django 3.1.2 on 2024-10-28 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0004_auto_20241028_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]