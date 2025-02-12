from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # field는 json으로 왔다갔다 하는 부분
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}} # 쓰기만 가능
        # password는 API 응답에서 보이지 안게 설정
        # field에 있는 내용은 보여주지만 패스워드는 안보일거야
    
                                        # **딕셔너리 형태로 키워드 가변인자
    def create(self, validated_data):   # {"key" : "value"}
        user = User.objects.create_user(**validated_data)
        # 상속받은 ModelSerializer를 이용하기 때문에
        # UserSerializer를 이용하면 키, 값을 그대로 데이터베이스에 저장되기 때문에
        # create_user() 함수를 이용해서 create 메서드를 재정의 해주어야 한다.
        return user