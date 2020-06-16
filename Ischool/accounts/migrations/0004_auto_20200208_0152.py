# Generated by Django 3.0.1 on 2020-02-08 09:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200207_0432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date_registered',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 2, 8, 1, 52, 52, 108005)),
        ),
        migrations.AlterField(
            model_name='student',
            name='myclass',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='accounts.Myclass'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='date_registered',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 2, 8, 1, 52, 52, 108005)),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='myclass',
            field=models.ManyToManyField(to='accounts.Myclass'),
        ),
    ]