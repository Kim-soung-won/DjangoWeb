from django.urls import path, re_path
from . import views

urlpatterns = [
    path('create', views.TaskCreate.as_view(), name='create'),
    path('select', views.TaskSelect.as_view(), name='select'),
    path('delete', views.TaskDelete.as_view(), name='delete'),
    path('update', views.TaskUpdate.as_view(), name='update'),
    path('getList', views.TaskListByUser.as_view(), name="getList")
]
