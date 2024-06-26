# Generated by Django 5.0.3 on 2024-06-08 15:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0068_site'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageCoverModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='images/product/cover/')),
            ],
            options={
                'verbose_name': 'Image Cover',
                'verbose_name_plural': 'Image Covers',
            },
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='cover_image',
        ),
        migrations.CreateModel(
            name='AddCoverImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('gender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.productgendermodel')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cover_image_product', to='product.productmodel')),
            ],
        ),
    ]
