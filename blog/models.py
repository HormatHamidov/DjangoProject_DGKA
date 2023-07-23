from django.db import models


# Create your models here.
# class Student(models.Model):
#     name = models.CharField(max_length=30)
#     surname = models.CharField(max_length=30)

#     def __str__(self):
#         return self.name


class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=200)
    article_image = models.FileField(blank=True, null=True) 
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title