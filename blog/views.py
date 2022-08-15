from ast import Raise
from rest_framework.response import Response 
from urllib.parse import urlparse
from rest_framework import status
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from blog.generic import GenericPagnication
from blog.models import BlogModel
from blog.serializers import BlogDetailSerializer,BlogListSerializer
from rest_framework.filters import SearchFilter
from blog.utils import scrapping_wpbeginner,scrapping_makeuseof,scrap_elementor_site

class BlogDetailViewAPI(ListCreateAPIView):

    pagination_class = GenericPagnication
    filter_backends = [SearchFilter]
    queryset = BlogModel.objects.all()
    serializer_class = BlogListSerializer
    search_fields = [
        'title',
        'description',
        'username'
    ]


    # def post(self, request, *args, **kwargs):
    #     request_data = request.data
    #     print(request_data,'data')
    #     serializer = BlogDetailSerializer(data=request_data)
    #     print(serializer)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,status=status.HTTP_201_CREATED)

    #     else:
    #         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class BlogDeleteUpdateAPi(RetrieveUpdateDestroyAPIView):

    lookup_field = 'pk'
    queryset = BlogModel.objects.all()
    serializer_class = BlogDetailSerializer

    def delete(self,request,pk):
        obj = self.get_object()
        data = obj.delete()
        return Response({"detail":"deleted successfully"})


class DefaultSaveAPI(ListCreateAPIView):

    def post(self,request):
        request_data = request.data.get('url',None)
        if request_data:
            requested_data_domain = urlparse(request_data).netloc
            if requested_data_domain =='www.wpbeginner.com':
                blog_list = scrapping_wpbeginner(request_data)
            elif requested_data_domain == 'elementor.com':
                blog_list = scrap_elementor_site(request_data)
            elif requested_data_domain == 'www.makeuseof.com':
                blog_list = scrapping_makeuseof(request_data)
            else:
                return Response({"detail":"Please provide url That is in readme File"},
                    status=status.HTTP_400_BAD_REQUEST)
            for blog in blog_list:
                blog['username'] = 'Admin'
                blog_save = BlogModel.objects.create(**blog)
            blog_data =  BlogModel.objects.all()
            serializer = BlogListSerializer(blog_data,many=True)
            
        return Response(serializer.data,status=status.HTTP_200_OK)

