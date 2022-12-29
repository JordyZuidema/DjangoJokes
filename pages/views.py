from django.shortcuts import render
from django.views.generic import TemplateView

class HomepageView(TemplateView):
    template_name = "pages/home.html"
    
class AboutUsView(TemplateView):
    template_name = "pages/about_us.html"



