# Generated by Django 5.0.3 on 2024-04-14 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0045_remove_productsubcategorymodel_product_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='addsubcategorymodel',
            options={},
        ),
        migrations.RemoveField(
            model_name='addsubcategorymodel',
            name='slug',
        ),
    ]