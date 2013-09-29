import os
from django.contrib.auth import logout, get_user
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
import time
from subscription.ExpItem import ExpItem
from subscription.SharedExp import SharedExp
from subscription.models import Experience

APP_ROOT = os.path.dirname(globals()['__file__'])


def home(request):
    if isValidateUser(request):
        allExperiences = Experience.objects.all()
        blogItems = convertToBlogItems(allExperiences)
        return render_to_response('home.html', {'blogItems': blogItems}, context_instance=RequestContext(request))
    else:
        return render_to_response('index.html', context_instance=RequestContext(request))

def convertToBlogItems(allExperiences):
    blogItems = []
    for experience in allExperiences:
        expItem = ExpItem(experience)
        blogItems.append(expItem)
    return blogItems

def about(request):
    return render_to_response('about.html', context_instance=RequestContext(request))

def getExperienceImages(img_links):
    if not img_links:
        return []
    else:
        return img_links.split(',')

def experiencePage(request, id):
    experience = Experience.objects.get(pk=id)
    #TODO check out if experience is null or not
    imagesOfExperience = getExperienceImages(experience.img_links)
    return render_to_response('experience.html', {'experience': experience,'images':imagesOfExperience},
        context_instance=RequestContext(request))


def logout_user(request):
    logout(request)
    response = redirect('subscription.views.home')
    response.delete_cookie('facebook')
    return response

########## Share experience
def generateFileName(extension,i):
    return str(int(time.time())) + str(i) + "." + extension

def createFolderForCurrentUser(userPath):
    userPath = "static" + userPath
    folderPath = os.path.join(APP_ROOT,userPath)
    if not os.path.isdir(folderPath):
        os.makedirs(folderPath)
    return folderPath


def getUserFolder(currentUserName):
    folderPath = "/pictures/" + currentUserName
    return folderPath


def save_image_files(request):
    images = []
    i = 0
    if request.FILES is not None:
        for fileName,file in request.FILES.iteritems():
            name = generateFileName(file.name.split(".")[-1],i)
            i= i+1
            #TODO error check
            userFolder = getUserFolder(get_user(request).username)

            imgFolder = createFolderForCurrentUser(userFolder)

            filePath = os.path.join(APP_ROOT, imgFolder, name)

            images.append(userFolder + "/" + name)

            with open(filePath, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
    return images


def isValidateUser(request):
    return True
#    current_user = get_user(request)
#    if (not (current_user is None)) and current_user.is_authenticated():
#        return True
#    else:
#        return False


def share(request):
    if request.method == 'POST':
        if isValidateUser(request):
            images = save_image_files(request)
            experience = SharedExp(request.POST).getExperience(request,images)
            experience.save()
            return redirect('subscription.views.home')
        else:
            return render_to_response('share.html', context_instance=RequestContext(request))
    else:
        return render_to_response('share.html', context_instance=RequestContext(request))

