# Generated by Django 5.0.2 on 2024-03-01 16:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartsettingmodel',
            options={'verbose_name': 'Banner-Cart page', 'verbose_name_plural': 'Banner-Cart page'},
        ),
        migrations.AlterModelOptions(
            name='contactmodel',
            options={},
        ),
        migrations.AlterModelOptions(
            name='productsettingmodel',
            options={'verbose_name': 'Size Chart - Shop Page', 'verbose_name_plural': 'Size Chart - Shop Page'},
        ),
        migrations.RemoveField(
            model_name='contactmodel',
            name='address',
        ),
        migrations.RemoveField(
            model_name='contactmodel',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='contactmodel',
            name='name',
        ),
        migrations.RemoveField(
            model_name='homesettingmodel',
            name='middle_video_title',
        ),
        migrations.RemoveField(
            model_name='middlebannerslidermodel',
            name='title',
        ),
        migrations.AddField(
            model_name='cartsettingmodel',
            name='setting',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.homesettingmodel'),
        ),
        migrations.AddField(
            model_name='contactmodel',
            name='number',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='contactmodel',
            name='setting',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.homesettingmodel'),
        ),
        migrations.AddField(
            model_name='middlebannerslidermodel',
            name='setting',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.homesettingmodel'),
        ),
        migrations.AddField(
            model_name='productsettingmodel',
            name='setting',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.homesettingmodel'),
        ),
        migrations.AlterField(
            model_name='bannerhomemodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/home/banner'),
        ),
        migrations.AlterField(
            model_name='bannerhomemodel',
            name='setting',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.homesettingmodel'),
        ),
        migrations.AlterField(
            model_name='cartsettingmodel',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='images/cart/setting'),
        ),
        migrations.AlterField(
            model_name='contactmodel',
            name='priority',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homesettingmodel',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='images/home/', verbose_name='Section 6 Image'),
        ),
        migrations.AlterField(
            model_name='homesettingmodel',
            name='button_banner',
            field=models.ImageField(blank=True, null=True, upload_to='images/home/', verbose_name='Section 4 Image'),
        ),
        migrations.AlterField(
            model_name='homesettingmodel',
            name='button_video',
            field=models.FileField(blank=True, null=True, upload_to='videos/home', verbose_name='Section 7 Video'),
        ),
        migrations.AlterField(
            model_name='homesettingmodel',
            name='button_video_description',
            field=models.TextField(blank=True, null=True, verbose_name='Section 7 Description'),
        ),
        migrations.AlterField(
            model_name='homesettingmodel',
            name='button_video_title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Section 7 Title'),
        ),
        migrations.AlterField(
            model_name='homesettingmodel',
            name='footer_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/home/footer', verbose_name='Section 8 Image'),
        ),
        migrations.AlterField(
            model_name='homesettingmodel',
            name='middle_description',
            field=models.TextField(blank=True, null=True, verbose_name='Section 2 Description'),
        ),
        migrations.AlterField(
            model_name='homesettingmodel',
            name='middle_title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Section 2 Title'),
        ),
        migrations.AlterField(
            model_name='homesettingmodel',
            name='middle_video',
            field=models.FileField(blank=True, null=True, upload_to='videos/home', verbose_name='Section 5 Video'),
        ),
        migrations.AlterField(
            model_name='homesettingmodel',
            name='middle_video_description',
            field=models.TextField(blank=True, null=True, verbose_name='Section 5 Description'),
        ),
        migrations.AlterField(
            model_name='homesettingmodel',
            name='top_description',
            field=models.TextField(blank=True, null=True, verbose_name='Section 1 Description'),
        ),
        migrations.AlterField(
            model_name='homesettingmodel',
            name='top_title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Section 1 Title'),
        ),
        migrations.AlterField(
            model_name='homesettingmodel',
            name='up_video',
            field=models.FileField(blank=True, null=True, upload_to='videos/home', verbose_name='Section 3 Video'),
        ),
        migrations.AlterField(
            model_name='homesettingmodel',
            name='up_video_description',
            field=models.TextField(blank=True, null=True, verbose_name='Section 3 Description'),
        ),
        migrations.AlterField(
            model_name='homesettingmodel',
            name='up_video_title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Section 3 Title'),
        ),
        migrations.AlterField(
            model_name='middlebannerslidermodel',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='images/home/'),
        ),
        migrations.AlterField(
            model_name='productsettingmodel',
            name='size_chart',
            field=models.ImageField(blank=True, null=True, upload_to='images/product/setting'),
        ),
    ]
