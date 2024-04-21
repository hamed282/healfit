# Generated by Django 5.0.3 on 2024-04-21 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0046_alter_addsubcategorymodel_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productmodel',
            options={'verbose_name': 'Item Groups', 'verbose_name_plural': 'Item Groups'},
        ),
        migrations.AlterModelOptions(
            name='productvariantmodel',
            options={'verbose_name': 'Items', 'verbose_name_plural': 'Items'},
        ),
        migrations.AddField(
            model_name='productmodel',
            name='descriptions',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
