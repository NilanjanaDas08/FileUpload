from django.db import models
import uuid

# Create your models here.
class FileUpload(models.Model):
    filename=models.FileField(upload_to='uploads/')
    original_filename=models.CharField(max_length=255,blank=True)
    size=models.IntegerField(blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.original_filename}"