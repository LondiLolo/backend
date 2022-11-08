from xml.etree.ElementInclude import include
from django.urls import path
from.views import displayTime, displayContact, MyViews, book_list, Post_list, post_detail, loginView, contactview
from .import views

app_name = 'blog'

urlpatterns = [
    path("books_list/" , book_list),
    path("", Post_list),
    path("contact/", displayContact, name="contact"),
    path("about/", contactview, name="about"),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name='post_detail'),
    path('login/', views.loginView, name="login"),
    path('profile/', views.profileView, name='profile'),
    path("logout/", views.logout_view, name='logout'),
    path('home/', MyViews.as_view, name="home")

]