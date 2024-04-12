# Generated by Django 5.0.3 on 2024-04-10 22:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_alter_productmodel_image1_alter_productmodel_image2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_product', to='product.productcategorymodel'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]