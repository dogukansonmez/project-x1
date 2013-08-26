import os
from django.contrib.auth import logout, get_user
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from exofus.settings import MEDIA_ROOT
from subscription.ExpItem import ExpItem
from subscription.SharedExp import SharedExp
from subscription.models import Experience, Comment


def home(request):
    allExperiences = Experience.objects.all()
    blogItems = convertToBlogItems(allExperiences)
    return render_to_response('home.html', {'blogItems': blogItems}, context_instance=RequestContext(request))


def about(request):
    return render_to_response('about.html', context_instance=RequestContext(request))


def save_image_files(request):
    file = request.FILES['file1']
        # Other data on the request.FILES dictionary:
        #   filesize = len(file['content'])
        #   filetype = file['content-type']

    with open('/Users/dogukansonmez/sonmez/django/project-x1/subscription/static/pictures/first.jpg', 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)


def share(request):
    if request.method == 'POST':
        myuser = get_user(request)
        print myuser.first_name
        print request.user.last_name
        print myuser.username
        print myuser.email
        save_image_files(request)
        experience = SharedExp(request.POST).getExperience()
        return render_to_response('share.html', context_instance=RequestContext(request))
    else:
        return render_to_response('share.html', context_instance=RequestContext(request))


def experiencePage(request, id):
    experience = Experience.objects.get(pk=id)
    comments= Comment.objects.filter(experience=id).all()
    return render_to_response('experience.html', {'experience': experience, 'comments': comments},
        context_instance=RequestContext(request))


def convertToBlogItems(allExperiences):
    blogItems = []
    for experience in allExperiences:
        blogItems.append(ExpItem(experience))
    return blogItems

def logout_user(request):
    logout(request)
    response = redirect('subscription.views.home')
    response.delete_cookie('facebook')
    return response
