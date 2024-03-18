from rest_framework.views import APIView
from .models import Task
from rest_framework.response import Response
from datetime import datetime
from django.core.paginator import Paginator
from django.shortcuts import render


class TaskCreate(APIView):

    def post(self, request):
        user_id = request.data['user_id']
        todo_id = request.data['todo_id']
        name = request.data['name']

        if Task.objects.filter(id=todo_id).exists():
            return Response(dict(msg="존재하는데.. 사실 자동으로 해야하거등여"))
        task = Task.objects.create(id=todo_id,user_id=user_id, name=name, start_date=datetime.now(), state=0)

        return Response(dict(
            msg="todo 생성 완료",
            user_id=user_id,
            task_id=task.id,
            name=task.name,
            start_date=task.start_date.strftime('%Y-%m-%d'),
        ))
class TaskSelect(APIView):
    def post(self, request):
        tasks = Task.objects.all()
        task_list = []
        for task in tasks:
            task_list.append(dict(
                id=task.id,
                name=task.name,
                done=task.state,
            ))
        return Response(dict(tasks=task_list))
class TaskDelete(APIView):
    def delete(self, request):
        todo_id = request.data['todo_id']
        task = Task.objects.get(id=todo_id)
        if task is None:
            return Response(dict(msg="없는데 어떻게 삭제해.."))
        task.delete()

        return Response(dict(msg="삭제끝"))
class TaskUpdate(APIView):
    def put(self, request):
        todo_id = request.data['todo_id']
        task = Task.objects.get(id=todo_id)
        if task is None:
            return Response(dict(msg="없는데 어떻게 완료해.."))
        if task.state == 0:
            task.state = Task.objects.update(state=1)
            return Response(dict(msg="완료!"))
        task.state = Task.objects.update(state=0)
        return Response(dict(msg="미완료!"))
class TaskListByUser(APIView):
    def get(self, request):
        tasks = Task.objects.filter(user_id=request.data['user_id'])
        paginator = Paginator(tasks, 10)
        page_number = request.data['page_number']
        page_obj = paginator.get_page(page_number)
        task_list = []
        for task in page_obj:
            print(task.id)
            task_list.append(dict(
                id=task.id,
                name=task.name,
                userId=task.user_id,
                done=task.state,
            ))
        return Response(dict(tasks=task_list))