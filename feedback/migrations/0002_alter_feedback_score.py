# Generated by Django 4.1.3 on 2022-11-26 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='score',
            field=models.IntegerField(choices=[(1, 'Poor'), (2, 'Bad'), (3, 'Ok'), (4, 'Good'), (5, 'Excellent')]),
        ),
    ]