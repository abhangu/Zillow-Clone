# Generated by Django 3.1.2 on 2020-11-18 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home_listing', '0001_initial'),
        ('core', '0003_auto_20201118_0320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=100)),
                ('offered_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_why', models.TextField(blank=True, null=True)),
                ('home_listing', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home_listing.listing')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.user')),
            ],
            options={
                'db_table': 'application',
            },
        ),
    ]