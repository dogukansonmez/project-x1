import datetime
from django.db.models import DateTimeField

__author__ = 'dogukansonmez'

class ExpItem:

    def __init__(self, experience):
        self.id = experience.id
        self.type = experience.type
        self.title = experience.title
        #self.tags = experience.tags
        date = experience.postDate
        self.postDate = "Post Date: " + str(date.day) + ' of ' + date.strftime("%B") + '  ' + str(date.year)
        if not not experience.img_links:
            #TODO Validate Image
            self.image = experience.img_links.split(',')[0]
        self.text = experience.description[:100]
        self.vote = experience.vote


