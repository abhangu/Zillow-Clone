# Generated by Django 3.1.2 on 2020-11-26 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('favorites', '0002_auto_20201126_0956'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favoritelisting',
            old_name='home_listing',
            new_name='listing',
        ),
    ]
