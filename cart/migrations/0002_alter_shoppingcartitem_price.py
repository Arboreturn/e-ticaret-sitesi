# Generated by Django 4.1.2 on 2022-11-21 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingcartitem',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
