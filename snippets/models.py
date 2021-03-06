
from django.contrib.auth.models import User
from django.db import models



class Language(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    class Meta:
        verbose_name = "Language"
        verbose_name_plural = "Languages"
    
    def __str__(self):
        return self.name


class Snippet(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    create_date= models.DateTimeField(auto_now=False,auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    snippet = models.TextField()
    language = models.ForeignKey(Language,on_delete=models.CASCADE)
    public = models.BooleanField(default = False)    
        
    class Meta:
        verbose_name = "Snippet"
        verbose_name_plural = "Snippets"
    
    def __str__(self):
        return self.name
    
