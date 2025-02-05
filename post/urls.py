from django.urls import path
from .views import PostWrite, PostList

# 패턴 맵핑
urlpatterns = [
    path('write/', PostWrite.as_view()),
    path('list/', PostList.as_view())
]