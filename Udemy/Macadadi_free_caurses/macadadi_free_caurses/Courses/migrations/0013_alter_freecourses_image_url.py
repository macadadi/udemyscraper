# Generated by Django 3.2.5 on 2021-08-21 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0012_auto_20210821_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freecourses',
            name='image_url',
            field=models.CharField(max_length=500),
        ),
    ]