import calendar
import datetime
from django.contrib.auth import get_user
from subscription.models import Experience, User

__author__ = 'dogukansonmez'


class SharedExp:
    def __init__(self, httpRequest):
       self.title = httpRequest.get('title','')
       self.where = httpRequest.get('where','')
       self.when = httpRequest.get('when','')
       self.whitWhom = httpRequest.get('withwhom','')
       self.vote = httpRequest.get('radios','')
       self.description = httpRequest.get('description','')


    def getExperience(self,request,images):

        experience = Experience()
        experience.name = self.title
        experience.title = self.title
        experience.where = self.where
        experience.when = str(self.when)
        experience.withWhom = self.whitWhom
        experience.description = self.description
        experience.vote = self.vote
        if len(images) > 0:
            experience.img_links = ','.join(images)
            experience.type='typeA'
        else:
            experience.type='typeB'
        currentUser = get_user(request)
        try:
            user = User.objects.get(userID=str(currentUser.username))
        except User.DoesNotExist:
            user = User()
            user.firstName = currentUser.first_name
            user.lastName = currentUser.last_name
            user.userID = currentUser.username
            user.save()
            experience.owner = user
        else:
            experience.owner = user
        return experience


