# Generated by Django 3.2.5 on 2021-08-25 22:27

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0015_alter_freecourses_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freecourses',
            name='image_file',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255),
        ),
    ]