# Generated by Django 3.2.5 on 2021-08-21 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0008_alter_freecourses_image_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freecourses',
            name='category',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='freecourses',
            name='image_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='freecourses',
            name='image_url',
            field=models.CharField(max_length=500, unique=True),
        ),
        migrations.AlterField(
            model_name='freecourses',
            name='sub_category',
            field=models.CharField(max_length=200),
        ),
    ]