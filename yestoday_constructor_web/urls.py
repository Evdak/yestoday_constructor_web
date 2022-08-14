from django.contrib import admin
from django.urls import path, include
from .views import get_audio_file

urlpatterns = [
    path('', include('constructor.urls')),
    path('get-audio/<str:auidoname>', get_audio_file),
    path('getcourse/', include('getcourse.urls')),
    path('admin/', admin.site.urls),
]
