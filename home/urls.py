from django.conf.urls import url,include
from . import views


urlpatterns = [
    url(r'^$', views.HomePageView),
    url(r'^folio/', include('folio.urls')),
]
