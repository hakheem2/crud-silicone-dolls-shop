from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
import os
from pathlib import Path
from django.contrib.sitemaps.views import sitemap
from products.sitemaps import StaticViewSitemap, ProductSitemap  # adjust import path


sitemaps = {
    'static': StaticViewSitemap,
    'products': ProductSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # root URL → homepage
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('order/', include(('order.urls', 'order'), namespace='order')),
    path('', include('core.urls', namespace='core')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),    # global pages
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('blog/', TemplateView.as_view(template_name='blog.html'), name='blog'),
    path('faqs/', TemplateView.as_view(template_name='faq.html'), name='faq'),
    path('privacy-terms/', TemplateView.as_view(template_name='terms.html'), name='terms'),
]

if settings.DEBUG or os.environ.get('RAILWAY_STATIC_SERVE_MEDIA') == 'True':
    BASE_DIR = Path(__file__).resolve().parent.parent
    urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(BASE_DIR, 'static'))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)