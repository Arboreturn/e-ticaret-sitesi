# Generated by Django 4.1.2 on 2022-10-25 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_page_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=200, null=True),
        ),
    ]