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
       self.vote = httpRequest.get('vote','')
       self.description = httpRequest.get('description','')

    def getExperience(self):
        experience = Experience()
        experience.name = self.title
        experience.type='typeB'
        experience.title = self.title
        experience.where = self.where
        experience.when = str(self.when)
        experience.withWhom = self.whitWhom
        experience.description = self.description
        experience.vote = 10
        experience.commentCount=0
        #experience.postDate = datetime.datetime.today()
        return experience


