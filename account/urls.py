from django.urls import path
from .views import registerView
from .import views

app_name = 'account'

urlpatterns = [
    
    path('signup/', registerView, name='signup'),
    path('<pk>/update', views.UserEditView.as_view(), name='edit_profile')
]