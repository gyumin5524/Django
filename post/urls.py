from django.urls import path
from .views import PostWrite, PostList, PostDetail, PostUpdate, PostDelete

# 패턴 맵핑
urlpatterns = [
    path('write/', PostWrite.as_view()),
    path('list/', PostList.as_view()),
    path('detail/<int:pk>/', PostDetail.as_view()),
    path('update/<int:pk>/', PostUpdate.as_view()),
    path('delete/<int:pk>/', PostDelete.as_view()),
]