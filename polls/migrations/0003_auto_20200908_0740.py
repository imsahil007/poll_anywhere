# Generated by Django 3.1.1 on 2020-09-08 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20200908_0411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='question',
            field=models.CharField(max_length=250),
        ),
    ]
