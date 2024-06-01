from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import ProductModel, Site


class ProductWomenViewSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def get_urls(self, site=None, **kwargs):
        site = Site(domain='healfit.ae', name='healfit.ae')
        return super(ProductWomenViewSitemap, self).get_urls(site=site, **kwargs)

    def items(self):
        return ['product:product_list']

    def location(self, item):
        return '/list/women'


class ProductMenViewSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def get_urls(self, site=None, **kwargs):
        site = Site(domain='healfit.ae', name='healfit.ae')
        return super(ProductMenViewSitemap, self).get_urls(site=site, **kwargs)

    def items(self):
        return ['product:product_list']

    def location(self, item):
        return '/list/men'


class SnippetSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def get_urls(self, site=None, **kwargs):
        site = Site(domain='healfit.ae', name='healfit.ae')
        return super(SnippetSitemap, self).get_urls(site=site, **kwargs)

    def items(self):
        return ProductModel.objects.all()

