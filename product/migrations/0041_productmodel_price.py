# Generated by Django 5.0.3 on 2024-04-14 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0040_remove_productmodel_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
