from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect

# Create your views here.
from creatMedia.forms import CreateMediaForm


def createMedia(request):
    form = CreateMediaForm()

    if request.method == 'POST':
        data = {
            'encoding': 'utf-8',
            'csrfmiddlewaretoken': request.POST['csrfmiddlewaretoken'],
            'userName': request.POST['userName'],
            'image': str(datetime.now().timestamp()) + request.FILES['image'].name,
            'description': request.POST['description']
        }
        form = CreateMediaForm(data)
        if form.is_valid():
            imageName = str(datetime.now().timestamp()) + request.FILES['image'].name
            fs = FileSystemStorage()
            fs.save(imageName, request.FILES['image'])
            form.save()
            return redirect('/')
        else:
            print('The form is invalid: ', form.errors)
    context = {'form': form}
    return render(request, 'createMedia/createMedia.html', context)


def postMedia(request):
    if request.method == 'POST':
        userName = request.POST.get("userName")
        image = request.FILES['image']
        imageName = request.FILES['image'].name
        description = request.POST.get("description")
        print(userName)
        print(image)
        print(description)

        fs = FileSystemStorage()
        fs.save(imageName, image)
    return render(request, 'feeds/feeds.html')
