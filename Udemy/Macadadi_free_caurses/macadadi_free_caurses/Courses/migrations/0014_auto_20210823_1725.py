# Generated by Django 3.2.5 on 2021-08-23 14:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0013_alter_freecourses_image_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='freecourses',
            old_name='days_left',
            new_name='uploaded',
        ),
        migrations.RemoveField(
            model_name='freecourses',
            name='sub_category',
        ),
        migrations.AddField(
            model_name='freecourses',
            name='outcome',
            field=models.CharField(default=datetime.datetime(2021, 8, 23, 14, 25, 29, 425957, tzinfo=utc), max_length=5000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='freecourses',
            name='status',
            field=models.CharField(default=datetime.datetime(2021, 8, 23, 14, 25, 48, 940944, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]
