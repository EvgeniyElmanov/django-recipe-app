# Generated by Django 5.0.3 on 2024-03-22 12:53

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='recipe_images/'),
            preserve_default=False,
        ),
    ]