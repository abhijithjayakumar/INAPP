from django.urls import path,include
from blog import views


urlpatterns = [

    path('api/v1/blog/',views.BlogDetailViewAPI.as_view()),
    path('api/v1/blog/<int:pk>/',views.BlogDeleteUpdateAPi.as_view()),
    path('api/v1/blog-post-save/',views.DefaultSaveAPI.as_view()),


]