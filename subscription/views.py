import os
from django.contrib.auth import logout, get_user
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from exofus.settings import APP_DIR
from subscription.UserManager import UserManager
from subscription.ExpItem import ExpItem
from subscription.SharedExp import SharedExp
from subscription.models import Experience, Comment


def home(request):
    allExperiences = Experience.objects.all()
    blogItems = convertToBlogItems(allExperiences)
    return render_to_response('home.html', {'blogItems': blogItems}, context_instance=RequestContext(request))


def about(request):
    return render_to_response('about.html', context_instance=RequestContext(request))

def generateFileName(name):
    currentUserName = UserManager().getCurrentUser()
    return currentUserName + name

def save_image_files(request):
    if request.FILES is not None:
        for fileName,file in request.FILES.iteritems():
            name = generateFileName(file.name)
            filePath = os.path.join(APP_DIR, "media/pictures", name)
            with open(filePath, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
    #file1 = request.FILES['file1']
    #file2 = request.FILES['file2']
    #file3 = request.FILES['file3']
        # Other data on the request.FILES dictionary:
        #   filesize = len(file['content'])
        #   filetype = file['content-type']

def share(request):
    if request.method == 'POST':
        #myuser = get_user(request)
        #print myuser.first_name
        #print request.user.last_name
        #print myuser.username
        #print myuser.email
        save_image_files(request)
        experience = SharedExp(request.POST).getExperience()
        experience.save()
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
        expItem = ExpItem(experience)
        blogItems.append(ExpItem(experience))
    return blogItems

def logout_user(request):
    logout(request)
    response = redirect('subscription.views.home')
    response.delete_cookie('facebook')
    return response
