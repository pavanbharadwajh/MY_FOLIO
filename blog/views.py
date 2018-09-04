# from django.shortcuts import render
from django.views.generic import TemplateView
# def BlogView(request):
#      return render(request, 'blog/studio.html')

class BlogView(TemplateView):
     template_name = "blog/studio.html"