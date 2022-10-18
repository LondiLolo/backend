from django.urls import path
from.views import displayTime, displayContact, MyViews, book_list, Post_list, post_detail

app_name = 'blog'

urlpatterns = [
    path("books_list/" , book_list),
    path("", Post_list),
    path("contact/", displayContact),
    path("about/", MyViews.as_view()),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name='post_detail'),
]