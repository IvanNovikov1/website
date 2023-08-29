from django.urls import path
from .views import index, top_sellers, advertisement_post, advertisement_detail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='main-page'),
    path('top-sellers', top_sellers, name='top-sellers'),
    path('advertisement-post', advertisement_post, name='adv-post'),
    path('advertisement/<int:pk>', advertisement_detail, name='adv-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
