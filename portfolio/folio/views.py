from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class FolioPageView(TemplateView):
    template_name = "folio/folio.html"


