from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name='admin panel'),
    path('api/v1/docs', include_docs_urls(title='SurveyAPI')),
    path('api/v1/', include('accounts.urls'), name='accounts'),
    path('api/v1/', include('worksheets.urls'), name='worksheets'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
