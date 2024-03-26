from rest_framework.views import APIView
from .models import Task
from rest_framework.response import Response
from datetime import datetime
from common.common import TodoView, SuccessResponse, SuccessResponseWithData, ErrorResponse, CommonResponse
import logging

logger = logging.getLogger('django')


class Test(TodoView):
    def post(self, request):
        logger.info("TEST API START!!!!")
        logger.info("user id = "+self.user_id)
        logger.info("version = "+self.version)

        output_value1 = self.user_id + self.version

        logger.info("output_value1 = " + output_value1)


        logger.info("TEST API END!!!!!!!!!!!")

        return Response(status=200)


class TaskCreate(TodoView):
    def post(self, request):
        if self.user_id is None:
            #버젼 관리 이전 버젼에는 헤더에 없기 때문에 이렇게 한다.
            user_id = request.data.get("user_id",None)
        else:
            user_id = self.user_id
        todo_id = request.data.get('todo_id',None)
        name = request.data['name']

        if todo_id:
            task = Task.objects.create(id=todo_id, user_id=user_id, name=name, start_date=datetime.now(), state=0)
        else:
            task = Task.objects.create(user_id=user_id, name=name, start_date=datetime.now())

        if self.version >= "1.1":
            return SuccessResponseWithData(dict(id=task.id))
        else:
            return Response(data=dict(id=task.id))


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
    def post(self, request):
        todo_id = request.data['todo_id']
        task = Task.objects.get(id=todo_id)
        if task is None:
            return Response(dict(msg="없는데 어떻게 삭제해.."))
        task.delete()

        return Response(dict(msg="삭제끝"))


class TaskUpdate(APIView):
    def post(self, request):
        todo_id = request.data['todo_id']
        task = Task.objects.get(id=todo_id)
        if task is None:
            return Response(dict(msg="없는데 어떻게 완료해.."))
        if task.state == 0:
            task.state = Task.objects.update(state=1)
            return Response(dict(msg="완료!"))
        task.state = Task.objects.update(state=0)
        return Response(dict(msg="미완료!"))


class TaskListByUser(TodoView):
    def post(self, request):
        if self.user_id is None:
            #버젼 관리, 이전 버젼에는 헤더에 없기 때문에 이렇게 한다.
            user_id = request.data.get("user_id", None)
        else:
            user_id = self.user_id
        page_number = request.data.get('page_number', None)
        if user_id == "":
            tasks = []
        elif user_id:
            tasks = Task.objects.filter(user_id=user_id)
        else:
            tasks = Task.objects.filter()
        is_last_page = True
        if page_number is not None and page_number >= 0:
            if tasks.count() <= 10:
                pass
            elif tasks.count() <= (1 + page_number) * 10:
                tasks = tasks[page_number*10:]
            else:
                tasks = tasks[page_number*10:(1+page_number)*10]
                is_last_page = False
        else:
            pass
        task_list = []
        for task in tasks:
            print(task.id)
            task_list.append(dict(
                id=task.id,
                name=task.name,
                userId=task.user_id,
                done=task.state,
            ))
        if self.version >= "1.1":
            return SuccessResponseWithData(dict(tasks=task_list, is_last_page=is_last_page))
        else:
            return Response(dict(tasks=task_list, is_last_page=is_last_page))