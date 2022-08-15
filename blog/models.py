from django.db import models

# Create your models here.

def image_content(instance, filename):
    

    home_title, exts = filename.split('.')
    
    file_path = '{model_id}/{subfolder}.{ext}'.format(
         model_id=str(instance.name), subfolder=str(home_title), ext=exts) 
    return file_path 


class BlogModel(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=256,blank=True,null=True)
    title = models.CharField(max_length=256,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to = image_content, blank=True, null=True)
    created_at  =models.DateTimeField(auto_now_add=True,editable=False)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table ='blog_model'
        verbose_name ='Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return self.title


