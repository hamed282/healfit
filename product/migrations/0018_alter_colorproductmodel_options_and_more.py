# Generated by Django 5.0.2 on 2024-03-15 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_alter_colorproductmodel_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='colorproductmodel',
            options={'verbose_name': 'Color Product', 'verbose_name_plural': 'Color Product'},
        ),
        migrations.AlterModelOptions(
            name='productcategorymodel',
            options={'verbose_name': 'Product Category', 'verbose_name_plural': 'Product Category'},
        ),
    ]