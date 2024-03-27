from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',include('account.urls')),
    path('',include('corona_virus_app.urls')),
]

handler404 = "corona_virus_app.views.page404"

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)