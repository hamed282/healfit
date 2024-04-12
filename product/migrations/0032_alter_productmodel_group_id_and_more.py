# Generated by Django 5.0.3 on 2024-04-11 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0031_rename_product_id_productmodel_group_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='group_id',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productvariantmodel',
            name='item_id',
            field=models.CharField(default=1, max_length=100, verbose_name='Product ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productvariantmodel',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
