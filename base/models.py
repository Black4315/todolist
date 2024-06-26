from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title =models.CharField(("title"), max_length=200)
    desc =models.TextField(("description") ,null=True , blank=True)
    comp =models.BooleanField(("completed" ),default = False)
    created =models.DateTimeField ( auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['comp']
    
# Create your models here.
