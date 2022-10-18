from django.urls import path
from .views import ecomView, MyViews


urlpatterns = [
    path("", ecomView),
    path("about/", MyViews.as_view())
]