from django.contrib.auth import logout, get_user
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from subscription.ExpItem import ExpItem
from subscription.SharedExp import SharedExp
from subscription.imageManager import save_image_files
from subscription.models import Experience

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
    global activeImage
    experience = Experience.objects.get(pk=id)
    #TODO check out if experience is null or not
    imagesOfExperience = getExperienceImages(experience.img_links)
    itemImages = []

    if len(imagesOfExperience) > 0:
        activeImage = imagesOfExperience[0]

    if len(imagesOfExperience) > 1:
        itemImages = imagesOfExperience[1:]

    return render_to_response('experience.html',
                              {'experience': experience, 'images': imagesOfExperience, 'activeImage': activeImage,
                               'itemImages': itemImages},
                              context_instance=RequestContext(request))

def logout_user(request):
    logout(request)
    response = redirect('subscription.views.home')
    response.delete_cookie('facebook')
    return response


def isValidateUser(request):
    current_user = get_user(request)
    if (not (current_user is None)) and current_user.is_authenticated():
        return True
    else:
        return False

def share(request):
    if request.method == 'POST':
        if isValidateUser(request):
            images = save_image_files(request)
            experience = SharedExp(request.POST).getExperience(request, images)
            experience.save()
            return redirect('subscription.views.home')
        else:
            return render_to_response('share.html', context_instance=RequestContext(request))
    else:
        return render_to_response('share.html', context_instance=RequestContext(request))

