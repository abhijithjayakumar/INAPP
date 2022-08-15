from rest_framework.response import Response 
from rest_framework import status
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from blog.generic import GenericPagnication
from blog.models import BlogModel
from comment.models import CommentModel
from blog.serializers import BlogDetailSerializer
from comment.serializers import CommentDetailSerializer
from rest_framework.filters import SearchFilter


class CommentDetailApi(ListCreateAPIView):

    pagination_class = GenericPagnication
    filter_backends = [SearchFilter]
    queryset = CommentModel.objects.all()
    serializer_class = CommentDetailSerializer
    search_fields = [
        'username',
        'comment'
    ]

class CommentApi(RetrieveUpdateDestroyAPIView):

    pagination_class = GenericPagnication
    filter_backends = [SearchFilter]
    lookup_field = 'pk'
    queryset = CommentModel.objects.all()
    serializer_class = CommentDetailSerializer
    

    def delete(self,request,pk):
        obj = self.get_object()
        data = obj.delete()
        return Response({"detail":"deleted successfully"})

