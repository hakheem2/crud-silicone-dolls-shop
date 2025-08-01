# your_project/middleware/www_redirect.py

from django.http import HttpResponsePermanentRedirect

class WwwRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()
        if host.startswith("www."):
            new_url = request.build_absolute_uri().replace("://www.", "://")
            return HttpResponsePermanentRedirect(new_url)
        return self.get_response(request)
