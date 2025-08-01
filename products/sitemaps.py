from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Product



class HttpsSitemap(Sitemap):
    def get_urls(self, page=1, site=None, protocol=None):
        protocol = 'https'  # force https here
        return super().get_urls(page=page, site=site, protocol=protocol)

# Sitemap for static pages (simple URLs without parameters)
class StaticViewSitemap(HttpsSitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return ['home', 'about', 'contact', 'product_list', 'product_detail', 'blog', 'terms', 'faq']

    def location(self, item):
        return reverse(item)  # or your custom logic

class ProductSitemap(HttpsSitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return Product.objects.filter(is_active=True)

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, item):
        # Pass slug for reversing the 'product_detail' URL
        return reverse('product_detail', args=[item.slug])
