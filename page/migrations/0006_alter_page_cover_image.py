# Generated by Django 4.1.2 on 2022-10-25 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0005_alter_page_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='page'),
        ),
    ]
