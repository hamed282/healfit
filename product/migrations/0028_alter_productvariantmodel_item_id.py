# Generated by Django 5.0.3 on 2024-04-11 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0027_productvariantmodel_item_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvariantmodel',
            name='item_id',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Product ID'),
        ),
    ]