# Generated by Django 3.0.8 on 2020-07-21 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20200721_2250'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='Name',
            new_name='name',
        ),
    ]