'''
from django.contrib import admin
from django.urls import include, path

# from polls.views import IndexView


urlpatterns = [
    path('', include('polls.urls')),
    path('admin/', admin.site.urls),
]
'''


from django.contrib import admin
from django.urls import include, path

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('', include('polls.urls')),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('eventos/', include('eventos.urls')),
    path('galeria/', include('galeria.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

