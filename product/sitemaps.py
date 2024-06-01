from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Snippet


class StaticViewSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9
    def items(self):
        return ['product:product']

    def location(self, item):
        return reverse(item)


class SnippetSitemap(Sitemap):
    def items(self):
        return Snippet.objects.all()
