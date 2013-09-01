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
        self.postDate = date.strftime("%B") + ' - '  + str(date.day) + ' - ' + str(date.year)
        self.numberOfComments = experience.commentCount
        if not not experience.img_links:
            imgurl = experience.img_links.split(',')[0]
            self.image = "pictures/%s"%imgurl
        self.text = experience.description[:100]


