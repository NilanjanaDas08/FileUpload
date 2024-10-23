from .models import FileUpload
from django import forms

class FileUploadForm(forms.ModelForm):
    class Meta:
        model=FileUpload
        fields=['filename']