# Generated by Django 5.0.3 on 2024-06-08 15:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0072_delete_imagecovermodel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='addimagegallerymodel',
            name='gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.productgendermodel'),
        ),
    ]
