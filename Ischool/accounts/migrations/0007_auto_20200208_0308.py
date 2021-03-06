# Generated by Django 3.0.1 on 2020-02-08 11:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200208_0257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deadline',
            name='last_date',
        ),
        migrations.AddField(
            model_name='deadline',
            name='day',
            field=models.IntegerField(blank=True, default=0, max_length=2),
        ),
        migrations.AddField(
            model_name='deadline',
            name='hour',
            field=models.IntegerField(blank=True, default=0, max_length=2),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_registered',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 2, 8, 3, 8, 28, 243837)),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='date_registered',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 2, 8, 3, 8, 28, 243837)),
        ),
    ]
