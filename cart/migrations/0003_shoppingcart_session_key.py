# Generated by Django 4.1.2 on 2022-11-21 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_shoppingcartitem_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingcart',
            name='session_key',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
