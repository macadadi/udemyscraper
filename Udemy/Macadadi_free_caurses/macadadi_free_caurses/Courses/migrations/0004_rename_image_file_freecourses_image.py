# Generated by Django 3.2.5 on 2021-08-15 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0003_rename_image_f_freecourses_image_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='freecourses',
            old_name='image_file',
            new_name='image',
        ),
    ]
