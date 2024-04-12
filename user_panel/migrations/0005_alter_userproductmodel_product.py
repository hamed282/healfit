# Generated by Django 5.0.3 on 2024-04-12 11:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0037_productvariantmodel_slug'),
        ('user_panel', '0004_alter_userproductmodel_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userproductmodel',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_product', to='product.productvariantmodel'),
        ),
    ]
