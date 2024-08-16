from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('upload/', views.upload_image, name='upload_image'),
    # Otras rutas aquí
    path('', views.home, name='home'),
    path('show_posts/', views.show_posts, name='show_posts'),
    path('detail/<int:quillpost_id>/', views.quillpost_detail, name='detail'),
    path('form_blocks/', include('form_blocks.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)