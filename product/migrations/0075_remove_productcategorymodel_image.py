# Generated by Django 5.0.3 on 2024-06-29 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0074_remove_addimagegallerymodel_gender_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcategorymodel',
            name='image',
        ),
    ]
