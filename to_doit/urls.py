from django.urls import path, re_path
from . import views

urlpatterns = [
    path('create', views.TaskCreate.as_view(), name='create'),
    #path('select', views.TaskSelect.as_view(), name='select'),
    path('delete', views.TaskDelete.as_view(), name='delete'),
    path('toggle', views.TaskUpdate.as_view(), name='update'),
    path('select', views.TaskListByUser.as_view(), name="getList"),
    path('test', views.Test.as_view(), name="test")
]
