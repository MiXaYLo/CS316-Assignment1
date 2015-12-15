from django.conf.urls import url
from django.contrib import admin
from assignmentone.views import count

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^count/$', count)
]
