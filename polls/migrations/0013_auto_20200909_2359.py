# Generated by Django 3.1.1 on 2020-09-09 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20200909_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='choice_count',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
