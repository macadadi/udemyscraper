# Generated by Django 3.2.5 on 2021-08-15 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0005_rename_image_freecourses_image_real'),
    ]

    operations = [
        migrations.RenameField(
            model_name='freecourses',
            old_name='image_real',
            new_name='image_file',
        ),
    ]