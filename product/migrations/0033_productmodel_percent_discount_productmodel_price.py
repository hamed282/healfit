# Generated by Django 5.0.3 on 2024-04-11 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0032_alter_productmodel_group_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='percent_discount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
