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

urlpatterns = [

    path('', include('polls.urls')),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
]

