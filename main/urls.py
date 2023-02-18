from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('released', views.released, name='released'),
    path('released/<int:pk>',
         views.release_detail.as_view(),
         name='release-detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
