# Generated by Django 3.0.1 on 2020-02-03 19:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='chc',
            field=models.IntegerField(blank=True, default=1, max_length=2),
        ),
        migrations.AddField(
            model_name='student',
            name='chf',
            field=models.IntegerField(blank=True, default=1, max_length=2),
        ),
        migrations.AddField(
            model_name='student',
            name='chs',
            field=models.IntegerField(blank=True, default=1, max_length=2),
        ),
        migrations.AddField(
            model_name='student',
            name='phc',
            field=models.IntegerField(blank=True, default=1, max_length=2),
        ),
        migrations.AddField(
            model_name='student',
            name='phf',
            field=models.IntegerField(blank=True, default=1, max_length=2),
        ),
        migrations.AddField(
            model_name='student',
            name='phs',
            field=models.IntegerField(blank=True, default=1, max_length=2),
        ),
        migrations.AddField(
            model_name='student',
            name='rc',
            field=models.IntegerField(blank=True, default=1, max_length=2),
        ),
        migrations.AddField(
            model_name='student',
            name='rf',
            field=models.IntegerField(blank=True, default=1, max_length=2),
        ),
        migrations.AddField(
            model_name='student',
            name='rs',
            field=models.IntegerField(blank=True, default=1, max_length=2),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_registered',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 2, 3, 23, 2, 43, 765014)),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='date_registered',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 2, 3, 23, 2, 43, 765014)),
        ),
    ]
