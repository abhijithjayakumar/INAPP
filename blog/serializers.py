from rest_framework import serializers
from blog.models import BlogModel
from comment.serializers import CommentDetailSerializer


class BlogDetailSerializer(serializers.ModelSerializer):
    comments = CommentDetailSerializer(many=True)

    class Meta:
        model = BlogModel
        fields = '__all__'

class BlogListSerializer(serializers.ModelSerializer):

    class Meta:
        model =BlogModel
        fields = '__all__'

    # def create(self,validate_data):
    #     print(validate_data)
    #     return BlogModel.objects.create(**validate_data)

