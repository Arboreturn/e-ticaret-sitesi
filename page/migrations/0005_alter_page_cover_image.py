# Generated by Django 4.1.2 on 2022-10-25 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0004_alter_page_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='cover_image',
            field=models.ImageField(null=True, upload_to='page'),
        ),
    ]
