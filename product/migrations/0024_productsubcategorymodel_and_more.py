# Generated by Django 5.0.3 on 2024-04-11 06:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0023_rename_product_code_productmodel_product_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSubCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Product SubCategory',
                'verbose_name_plural': 'Product SubCategory',
            },
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_product', to='product.productsubcategorymodel'),
        ),
    ]
