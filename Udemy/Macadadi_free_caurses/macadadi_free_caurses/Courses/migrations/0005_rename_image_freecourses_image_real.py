# Generated by Django 3.2.5 on 2021-08-15 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0004_rename_image_file_freecourses_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='freecourses',
            old_name='image',
            new_name='image_real',
        ),
    ]
