from django.urls import path,include
from comment import views

urlpatterns = [
    path('api/v1/comment/',views.CommentDetailApi.as_view()),
    path('api/v1/comment/<int:pk>/',views.CommentApi.as_view())
]