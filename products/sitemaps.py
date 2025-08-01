from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Product


# Sitemap for static pages (simple URLs without parameters)
class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        # List of URL pattern names for static pages only (no parameters)
        return ['home', 'about', 'contact', 'product_list', 'blog', 'terms', 'faq']

    def location(self, item):
        return reverse(item)


# Sitemap for dynamic product pages (with slug)
class ProductSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        # Return active products queryset
        return Product.objects.filter(available=True)

    def lastmod(self, obj):
        return obj.created_at

    def location(self, item):
        # Pass slug for reversing the 'product_detail' URL
        return reverse('product_detail', args=[item.slug])
