from django.urls import path
from .views import UserSignUpListView, UserLoginListView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', UserSignUpListView.as_view(), name='user_sign_up'),
    path('login/', UserLoginListView.as_view(), name='user_login'),
    path('logout/', LogoutView.as_view(next_page='user_login'), name='user_logout'),
]