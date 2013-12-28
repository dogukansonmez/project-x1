from django.contrib.auth import logout, get_user
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from subscription.ExpItem import ExpItem
from subscription.ImageManager import save_image_files
from subscription.SharedExp import SharedExp
from subscription.models import Experience, User

####################################################################################
def home(request):
    if isValidUser(request):
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

####################################################################################
def about(request):
    if isValidUser(request):
        return render_to_response('about.html', context_instance=RequestContext(request))
    else:
        return render_to_response('aboutus.html', context_instance=RequestContext(request))

def aboutus(request):
    return render_to_response('aboutus.html', context_instance=RequestContext(request))


def getExperienceImages(img_links):
    if not img_links:
        return []
    else:
        return img_links.split(',')

####################################################################################
def experiencePage(request, id):
    if isValidUser(request):
        experience = Experience.objects.get(pk=id)
        #TODO check out if experience is null or not
        imagesOfExperience = getExperienceImages(experience.img_links)
        itemImages = []
        activeImage = ""
        if len(imagesOfExperience) > 0:
            activeImage = imagesOfExperience[0]

        if len(imagesOfExperience) > 1:
            itemImages = imagesOfExperience[1:]

        return render_to_response('experience.html',
                              {'experience': experience, 'images': imagesOfExperience, 'activeImage': activeImage,
                               'itemImages': itemImages},
                              context_instance=RequestContext(request))
    else:
        return render_to_response('index.html', context_instance=RequestContext(request))

####################################################################################
def logout_user(request):
    logout(request)
    response = redirect('subscription.views.home')
    response.delete_cookie('facebook')
    return response


def isValidUser(request):
    current_user = get_user(request)
    return (not (current_user is None)) and current_user.is_authenticated()


def isRealUser(request):
    current_user = get_user(request)
    if (not (current_user is None)) and (current_user.first_name.strip()):
        return True
    else:
        return False

####################################################################################
def share(request):
    if isValidUser(request):
        if request.method == 'POST':
            if (isValidUser(request) and isRealUser(request)):
                images = save_image_files(request)
                experience = SharedExp(request.POST).getExperience(request, images)
                experience.save()
                return redirect('subscription.views.home')
            else:
                return render_to_response('index.html', context_instance=RequestContext(request))
        else:
            return render_to_response('share.html', context_instance=RequestContext(request))
    else:
        return render_to_response('index.html', context_instance=RequestContext(request))


####################################################################################
def my_experiences(request):
    if isValidUser(request):
        blogItems = []
        try:
            current_user = get_user(request)
            user = User.objects.get(userID=current_user)
            myExperiences = Experience.objects.filter(owner=user)
            blogItems = convertToBlogItems(myExperiences)
        except ObjectDoesNotExist:
            print "Seems you don't have any experiences"
        return render_to_response('myexperiences.html', {'blogItems': blogItems},
                                  context_instance=RequestContext(request))
    else:
        return render_to_response('index.html', context_instance=RequestContext(request))

####################################################################################
def removeExperience(request, id):
    if isValidUser(request):
        Experience.objects.filter(id=id).delete()
        response = redirect('subscription.views.my_experiences')
        return response
    else:
        return render_to_response('index.html', context_instance=RequestContext(request))

####################################################################################
def page_not_found(request):
        return render_to_response('404.html', context_instance=RequestContext(request))

####################################################################################
def server_error(request):
        return render_to_response('500.html', context_instance=RequestContext(request))
