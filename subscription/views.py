import os
from django.contrib.auth import logout, get_user
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
import time
from subscription.UserManager import UserManager
from subscription.ExpItem import ExpItem
from subscription.SharedExp import SharedExp
from subscription.models import Experience, Comment

APP_ROOT = os.path.dirname(globals()['__file__'])

def home(request):
    allExperiences = Experience.objects.all()
    blogItems = convertToBlogItems(allExperiences)
    return render_to_response('home.html', {'blogItems': blogItems}, context_instance=RequestContext(request))


def about(request):
    return render_to_response('about.html', context_instance=RequestContext(request))

def generateFileName(extension):
    return str(int(time.time())) + "." + extension

def createFolderForCurrentUser(userPath):
    userPath = "static" + userPath
    folderPath = os.path.join(APP_ROOT,userPath)
    if not os.path.isdir(folderPath):
        os.makedirs(folderPath)
    return folderPath


def getUserFolder():
    currentUserName = UserManager().getCurrentUser()
    folderPath = "/pictures/" + currentUserName
    return folderPath


def save_image_files(request):
    images = []
    if request.FILES is not None:
        for fileName,file in request.FILES.iteritems():

            name = generateFileName(file.name.split(".")[-1])
            userFolder = getUserFolder()
            imgFolder = createFolderForCurrentUser(userFolder)

            filePath = os.path.join(APP_ROOT, imgFolder, name)

            images.append(userFolder + "/" + name)

            with open(filePath, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
    return images

def share(request):
    if request.method == 'POST':
        images = save_image_files(request)
        experience = SharedExp(request.POST).getExperience(images)
        experience.save()
        return redirect('subscription.views.home')
        #render_to_response('home.html', context_instance=RequestContext(request))
    else:
        return render_to_response('share.html', context_instance=RequestContext(request))


def getExperienceImages(img_links):
    return img_links.split(',')


def experiencePage(request, id):
    experience = Experience.objects.get(pk=id)
    #TODO check out if experience is null or not
    comments= Comment.objects.filter(experience=id).all()
    imagesOfExperience = getExperienceImages(experience.img_links)
    return render_to_response('experience.html', {'experience': experience, 'comments': comments,'images':imagesOfExperience},
        context_instance=RequestContext(request))


def convertToBlogItems(allExperiences):
    blogItems = []
    for experience in allExperiences:
        expItem = ExpItem(experience)
        blogItems.append(expItem)
    return blogItems

def logout_user(request):
    logout(request)
    response = redirect('subscription.views.home')
    response.delete_cookie('facebook')
    return response
