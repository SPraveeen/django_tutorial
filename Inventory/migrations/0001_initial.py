# Generated by Django 4.2.23 on 2025-08-01 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200, null=True)),
                ('product_code', models.CharField(max_length=200, null=True)),
                ('product_price', models.FloatField(default=0)),
                ('gst', models.IntegerField(default=0)),
            ],
        ),
    ]
