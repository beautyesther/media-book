from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from creatMedia.models import CreateMedia


def getFeeds(request):
    photos = CreateMedia.objects.all()
    context = {'photos': photos}
    return render(request, 'feeds/feeds.html', context)
