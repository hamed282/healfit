# Generated by Django 5.0.3 on 2024-06-30 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0075_remove_productcategorymodel_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcategorymodel',
            name='category_title',
        ),
    ]