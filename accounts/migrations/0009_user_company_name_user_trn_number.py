# Generated by Django 5.0.2 on 2024-03-27 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_rename_vat_number_addressmodel_emirats_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='company_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='trn_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
