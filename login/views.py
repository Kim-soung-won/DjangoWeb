from rest_framework.views import APIView
from rest_framework.response import Response
from .models import LoginUser
# make_password = 어떤 문장을 패스워드로 사용하기 위해 hash값으로 단방향 암호화, 단방향 암호화라 복호화가 불가능
from django.contrib.auth.hashers import make_password, check_password
from .serialize import LoginUserSerializer

class AppLogin(APIView):
    def post(self,request):
        user_id = request.data['user_id']
        user_pw = request.data['user_pw']
        # user_pw_encryted = make_password(user_pw)
        user = LoginUser.objects.filter(user_id=user_id).first()

        if user is None:
            return Response(dict(msg="해당 사용자가 없습니다."))

        if check_password(user_pw, user.user_pw):
            return Response(dict(msg="로그인 성공",
                                 user_id=user.user_id,
                                 birthday=user.birthday,
                                 gender=user.gender,
                                 email=user.email,
                                 name=user.name,
                                 age=user.age
                                 ))
        else:
            return Response(dict(msg="로그인 실패, 비밀번호 틀림"))


# APIView를 상속 받으면 서브함수로 POST, GET 매핑에 따라 분리할 수 있다. Like Spring
class RegistUser(APIView):
    def post(self, request):
        serializer = LoginUserSerializer(request.data)

        # 동일한 UserId가 있는지 체크
        if LoginUser.objects.filter(user_id=serializer.data['user_id']).exists():
            user = LoginUser.objects.filter(user_id=serializer.data['user_id']).first()
            data = dict(
                msg="이미 존재하는 데이터입니다.",
                user_id=user.user_id,
                user_pw=user.user_pw
            )
            return Response(data)

        user = serializer.create(request.data)

        return Response(data=LoginUserSerializer(user).data)