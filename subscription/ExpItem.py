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
        self.image = experience.img_links
        self.video =experience.video_links
        self.text = experience.description[:100]
        self.numberOfComments = experience.commentCount


