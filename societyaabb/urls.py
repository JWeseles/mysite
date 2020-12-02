from django.contrib import admin
from django.urls import include, path

# from polls.views import IndexView


urlpatterns = [
    path('', include('polls.urls')),
    #    path('', IndexView),
    path('admin/', admin.site.urls),
]

'''
urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]
'''
