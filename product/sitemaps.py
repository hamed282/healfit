from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import ProductModel


class ProductWomenViewSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return ['product:product_list']

    def location(self, item):
        return '/list/women'


class ProductMenViewSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return ['product:product_list']

    def location(self, item):
        return '/list/men'


class SnippetSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return ProductModel.objects.all()

