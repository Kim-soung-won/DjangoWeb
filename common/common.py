from rest_framework.response import Response
from rest_framework.views import APIView


class TodoView(APIView):
    user_id = ''
    version = ''
    def dispatch(self, request, *args, **kwargs):
# 클라이언트에서 API요청이 오면 Django가 이 요청이 get인지, post인지, put인지 구분하는 과정을 거친다.
# 그 과정을 수행하는 것이 dispatch이다.
# 이걸 상위 클래스에서 정의하면 자식 API의 dispatch가 수행되기 전에 먼저 수행된다.
# 이 dispatch가 작동한 뒤에 본래 매서드에서 정의한 dispatch가 수행된다.
        self.user_id = request.headers.get('id', False)
        self.version = request.headers.get('version', '1.1')
        return super(TodoView, self).dispatch(request, *args, **kwargs)


def CommonResponse(result_code, result_msg, data):
    #응답 코드, 응답 메세지, 응답 데이터를 넣으면
    return Response(
        status=200,
        data=dict(
            result_code=result_code,
            result_msg=result_msg,
            data=data
        )
    )

def SuccessResponse():
    return Response(
        status=200,
        data=dict(
            result_code=0,
            result_msg="success"
        )
    )

def SuccessResponseWithData(data):
    return Response(
        status=200,
        data=dict(
            result_code=0,
            result_msg="success",
            data=data
        )
    )

def ErrorResponse():
    return Response(
        status=200,
        data=dict(
            result_code=999,
            result_msg="error!!"
        )
    )