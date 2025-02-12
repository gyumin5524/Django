from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404


class PostList(APIView):
    def get(self, request):
        posts = Post.objects.all()
        #응답: 직렬화(serializer), 데이터베이스에서 가져온 데이터 raw데이터 -> json데이터
        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class PostDetail(APIView):
    def get(self, request, pk):
        # 처리 - id 값을 이용해서 상세페이지 글 가져오기
        post = get_object_or_404(id = pk)
        serializer = PostSerializer(post)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class PostWrite(APIView):
    def post(self, request):
        #응답 역직렬화, json데이터 -> raw데이터 
        serializer = PostSerializer(data = request.data) # data = 들어가면 역직렬화
        #사용자에게 받은 값은 유효성 검증이 필수(악성데이터인지 아닌지)
        if serializer.is_valid():
            serializer.save() #True, 저장
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class PostWrite(APIView):
    def post(self, request):
        #응답 역직렬화, json데이터 -> raw데이터 
        serializer = PostSerializer(data = request.data) # data = 들어가면 역직렬화
        #사용자에게 받은 값은 유효성 검증이 필수(악성데이터인지 아닌지)
        if serializer.is_valid():
            serializer.save() #True, 저장
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class PostUpdate(APIView):
    def put(self, request, pk):
        # 전체수정
        # 1. 어떤 데이터를 수정할 지 알아야 한다.
        # 2. 어떻게 수정해야할 지 알아야 한다.
        # 3. 실제로 수정
        # 4. 저장
        post = get_object_or_404(Post, id = pk) # <-디비
        data = request.data # <- 사용자한테서
        serializer = PostSerializer(post, data=data) # 직렬화, 역직렬화 양방향
        if serializer.is_valid():
            serializer.save() #True, 저장
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):

        post = get_object_or_404(Post, id = pk) # <-디비
        data = request.data # <- 사용자한테서
        serializer = PostSerializer(post, partial=data) # partial 부분수정
        if serializer.is_valid():
            serializer.save() #True, 저장
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class PostDelete(APIView):
    def delete(self, request, pk):
        # 처리 - id값을 이용해서 삭제
        # 1. id값을 통해서 해당 객체 가져오기
        post = Post.objects.get(id = pk)
        # 2. 삭제하기 
        post.delete()
    
        return Response({"message": "게시글이 삭제되었습니다."}, status = status.HTTP_204_NO_CONTENT)


