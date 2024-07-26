from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from upload.models import Image,Document,safedrug
from upload.forms import ImageForm,DocForm


def home(request):
    documents=DocForm(request.POST or None)

    if documents.is_valid():
        documents.save()

    return render(request, 'upload/home.html', {'documents':documents})

def Result(request):
    return render(request, 'upload/Result.html')

def NotResult(request):
    return render(request, 'upload/NotResult.html')


def simple_upload(request):
    all_t=safedrug.objects.filter(drugname__iexact=request)
    if all_t:
        return([e.drugname for e in safedrug.objects.filter(drugname__iexact=request)])
    else:
        return 


        #return(all_t)
        #return render(request, 'upload/simple_upload.html', {
            #'uploaded_file_url':uploaded_file_url 
        #})
    #return render(request, 'upload/simple_upload.html')

def hello(req):
    import easyocr
    import cv2
    import matplotlib.pyplot as plt
    from pylab import rcParams
    import numpy as np
    rcParams['figure.figsize'] = 8, 16
    cap = cv2.imread(req)
    hsv = cv2.cvtColor(cap, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    reader = easyocr.Reader(['en']) 
    result = reader.readtext(mask)
    #print(result)
    t=result[0][1]
    return(t)
    #return HttpResponse(t)

#return HttpResponse("hello")
# Create your views here.
def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            img_name=hello(img_obj.image.url[1:])
            drugname=simple_upload(img_name)

            return render(request, 'upload/index.html', {'form': form, 'img_obj': img_obj,'img_name':img_name,'drugname':drugname})
        #return(hello(img_obj.image.url[1:]))
    else:
        form = ImageForm()
    return render(request, 'upload/index.html', {'form': form})

