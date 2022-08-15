from django.db import models
from blog.models import BlogModel
# Create your models here.

class CommentModel(models.Model):
    id = models.AutoField(primary_key=True)
    blog = models.ForeignKey(
        BlogModel,
        on_delete=models.SET_NULL,
        blank=True,null=True,
        related_name="comments",
        verbose_name="Comment Blog"
        )
    username = models.CharField(max_length=256,blank=True,null=True)
    comment = models.TextField(blank=True,null=True)
    created_at  =models.DateTimeField(auto_now_add=True,editable=False)
    updated_at = models.DateTimeField(auto_now_add=True)

