from django.shortcuts import render,redirect
from .models import FileUpload
from .forms import FileUploadForm
from django.http import HttpResponse

# Create your views here.
def upload_file(request):
    if request.method=='POST':
        form=FileUploadForm(request.POST,request.FILES)
        if form.is_valid():
            uploaded_file=form.cleaned_data['filename']

            if uploaded_file.size>2*1024*1024:
                return HttpResponse('Not expected')
            if not uploaded_file.name.endswith(('.pdf','.jpg','.png','.jpeg')):
                return HttpResponse('Only PDF,JPG and PNG files are accepted')
            
            form.save()
            return redirect('success')
    else:
        form=FileUploadForm()
    return render(request,'upload.html',{'form':form})

def success(request):
    return render(request,'success.html')

            
