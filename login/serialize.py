# 직렬화 기능
from rest_framework import serializers
from .models import LoginUser
from django.contrib.auth.hashers import make_password


class LoginUserSerializer(serializers.ModelSerializer):
    # rest_famework에서 제공하는 serializers 상속받아 기능 생성
    def create(self, validated_data):
        # create = serializers를 사용해 직렬화를 할 때 어떤 로직이 들어갈지 넣는 부분
        validated_data['user_pw'] = make_password(validated_data['user_pw'])
        user = LoginUser.objects.create(**validated_data)
        # 직렬화된 Model을 create
        return user

    def validate(self, attrs):
        return attrs

    class Meta:
        model = LoginUser
        fields = ('user_id', 'user_pw', 'birthday', 'gender', 'email', 'name', 'age')
