from django.urls import path, re_path
from .views import RegistUser, AppLogin

urlpatterns = [
    path('regist_user', RegistUser.as_view(), name='regist_user'),
    path('app_login', AppLogin.as_view(), name='app_login')
]