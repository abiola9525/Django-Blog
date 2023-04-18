from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"Publish"),
    (2,"Delete")
)

class posts(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    metades = models.CharField(max_length=50, default="new post")
    status = models.IntegerField(choices=STATUS, default=0)
    
    class Meta:
        verbose_name_plural = "Posts"
        ordering = ['-created_on']
        
    def __str__(self):
        return self.title
    