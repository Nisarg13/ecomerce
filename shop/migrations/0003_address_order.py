# Generated by Django 3.0.8 on 2020-07-19 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('address_line1', models.CharField(blank=True, max_length=200)),
                ('address_line2', models.CharField(blank=True, max_length=200)),
                ('city', models.CharField(blank=True, max_length=200)),
                ('country', models.CharField(blank=True, max_length=200)),
                ('zip_code', models.CharField(blank=True, max_length=200)),
                ('contact_no', models.CharField(blank=True, max_length=200)),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=0)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Ordered', 'Ordered'), ('Shipped', 'Shipped'), ('Dispatched', 'Dispatched'), ('Delivered', 'Delivered')], max_length=20)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Address')),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Customer')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product')),
            ],
        ),
    ]