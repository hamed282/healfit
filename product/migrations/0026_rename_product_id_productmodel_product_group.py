# Generated by Django 5.0.3 on 2024-04-11 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0025_remove_productmodel_percent_discount_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productmodel',
            old_name='product_id',
            new_name='product_group',
        ),
    ]
