# Generated by Django 4.1.3 on 2022-12-17 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_alter_payment_transaction_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkoutaddress',
            name='city',
            field=models.CharField(default='DEFAULT', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='checkoutaddress',
            name='apartment_address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
