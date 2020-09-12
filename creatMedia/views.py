from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect

# Create your views here.
from creatMedia.forms import CreateMediaForm


def createMedia(request):
    form = CreateMediaForm()

    if request.method == 'POST':
        extension = request.FILES['image'].name.split('.')
        time_of_post = str(datetime.now().timestamp()) + '.' + extension[len(extension) - 1]
        data = {
            'encoding': 'utf-8',
            'csrfmiddlewaretoken': request.POST['csrfmiddlewaretoken'],
            'userName': request.POST['userName'],
            'image': time_of_post,
            'description': request.POST['description']
        }
        form = CreateMediaForm(data)
        if form.is_valid():
            image_name = time_of_post
            fs = FileSystemStorage()
            fs.save(image_name, request.FILES['image'])
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
