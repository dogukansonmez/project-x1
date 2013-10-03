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
            images = experience.img_links.split(',')
            self.activeImage = []
            self.itemImages = []
            if len(images) == 1:
                self.activeImage = images[0]
            elif len(images) > 1:
                self.activeImage = images[0]
                self.itemImages = images[1:]
        self.text = experience.description[:100]
        self.vote = experience.vote


