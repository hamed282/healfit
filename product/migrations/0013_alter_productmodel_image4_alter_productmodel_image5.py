# Generated by Django 5.0.2 on 2024-03-12 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_productcategorymodel_category_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='images/product/'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='images/product/'),
        ),
    ]
