# Generated by Django 4.1.3 on 2022-12-18 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='status',
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]
