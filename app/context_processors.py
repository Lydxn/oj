from django.conf import settings

def site_info(request):
    return {
        'SITE_NAME': settings.SITE_NAME
    }
