from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
# class HomePageView(TemplateView):
#     template_name = "home/index.html"
    # def get(self, request, **kwargs):
    #     return render(request, 'home/index.html', context=None)

def HomePageView(request):
    return render(request, 'home/index.html'
    )

class AboutPageView(TemplateView):
    template_name = "home/about.html"

