from django.urls import path
from .views import HomepageView, AboutUsView

app_name = "pages"
urlpatterns = [
    path("", HomepageView.as_view(), name="homepage"),
    path("about-us/", AboutUsView.as_view(), name="about-us"),

]
