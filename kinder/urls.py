from django.urls import path
from django.contrib import admin
from kinder_app.views import *
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('kinder_app.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]+static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)