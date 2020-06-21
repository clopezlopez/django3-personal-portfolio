from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from portfolio import views 


urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)