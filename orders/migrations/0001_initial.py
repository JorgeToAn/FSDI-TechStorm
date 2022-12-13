# Generated by Django 4.1.3 on 2022-12-01 04:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import orders.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='uploads/products')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, validators=[orders.models.validate_price])),
                ('category', models.CharField(choices=[('COMPUTER', 'Computer'), ('ELECTRONICS', 'Electronics'), ('GAMING', 'Gaming'), ('OFFICE', 'Office'), ('NETWORKING', 'Networking'), ('THEATER', 'Theater'), ('TOYS', 'Toys'), ('SOFTWARE', 'Software'), ('AUDIO_VIDEO', 'Audio & Video')], max_length=80)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('quantity', models.PositiveIntegerField(default=1, validators=[orders.models.validate_quantity])),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('ordered_date', models.DateTimeField()),
                ('ordered', models.BooleanField(default=False)),
                ('products', models.ManyToManyField(to='orders.orderproduct')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]