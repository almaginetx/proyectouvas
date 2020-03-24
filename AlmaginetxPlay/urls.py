#AlmaginetxPlay URL Configuration
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^$', include('app.urls')),
    url(r'^', include('app.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns.append(
        # /media/:<mixed>path/
        url(
            regex=r'^media/(?P<path>.*)$',
            view='django.views.static.serve',
            kwargs={'document_root': settings.MEDIA_ROOT}))