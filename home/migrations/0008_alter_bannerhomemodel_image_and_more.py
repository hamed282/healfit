# Generated by Django 5.0.2 on 2024-03-01 15:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_homesettingmodel_banner_and_more'),
    ]

    operations = [
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
            model_name='cartsettingmodel',
            name='setting',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.homesettingmodel'),
        ),
        migrations.AlterField(
            model_name='contactmodel',
            name='address',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='contactmodel',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='images/social_media/'),
        ),
        migrations.AlterField(
            model_name='contactmodel',
            name='name',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='contactmodel',
            name='priority',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contactmodel',
            name='setting',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.homesettingmodel'),
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
            name='middle_video_title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Section 5 Title'),
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
            model_name='middlebannerslidermodel',
            name='setting',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.homesettingmodel'),
        ),
        migrations.AlterField(
            model_name='middlebannerslidermodel',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='productsettingmodel',
            name='setting',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.homesettingmodel'),
        ),
        migrations.AlterField(
            model_name='productsettingmodel',
            name='size_chart',
            field=models.ImageField(blank=True, null=True, upload_to='images/product/setting'),
        ),
    ]