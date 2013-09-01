import calendar
import datetime
from subscription.models import Experience

__author__ = 'dogukansonmez'


class SharedExp:
    def __init__(self, httpRequest):
       self.title = httpRequest.get('title','')
       self.where = httpRequest.get('where','')
       self.when = httpRequest.get('when','')
       self.whitWhom = httpRequest.get('whitWhom','')
       self.vote = httpRequest.get('radios','')
       self.description = httpRequest.get('description','')


    def getExperience(self,images):
        experience = Experience()
        experience.name = self.title
        experience.title = self.title
        experience.where = self.where
        experience.when = str(self.when)
        experience.withWhom = self.whitWhom
        experience.description = self.description
        experience.vote = self.vote
        experience.commentCount=0
        if len(images) > 0:
            experience.img_links = ','.join(images)
            experience.type='typeA'
        else:
            experience.type='typeB'
        return experience


