# Generated by Django 5.0.3 on 2024-04-23 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0057_addimagegallerymodel_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='addimagegallerymodel',
            options={'verbose_name': 'Product Image Gallery', 'verbose_name_plural': 'Product Image Gallery'},
        ),
        migrations.DeleteModel(
            name='ProductImageGalleryModel',
        ),
    ]
