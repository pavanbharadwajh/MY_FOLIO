from django.conf.urls import url,include
from . import views
from django.views.generic import ListView,DateDetailView
from .models import Post


urlpatterns = [    url(r'^$', ListView.as_view(queryset = Post.objects.all().order_by("-date"), template_name ="blog/studio.html"))
    ]