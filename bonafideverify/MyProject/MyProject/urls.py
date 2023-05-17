from django.contrib import admin
from django.urls import path
from UploadFiles import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('createfile',views.createfile,name="createfile"),
    path('check/',views.hello,name="hello"),
    path('uploadfile/',views.uploadfile,name="uploadfile"),
    
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
