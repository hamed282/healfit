# Generated by Django 5.0.3 on 2024-04-14 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0037_productvariantmodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
