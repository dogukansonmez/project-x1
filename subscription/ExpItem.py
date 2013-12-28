
__author__ = 'dogukansonmez'


class ExpItem:
    def __init__(self, experience):
        self.id = experience.id
        self.type = experience.type
        self.title = experience.title
        #self.tags = experience.tags
        date = experience.when
        self.postDate = str(date.day) + ' of ' + date.strftime("%B") + '  ' + str(date.year)
        images = experience.img_links.split(',')
        if not not experience.img_links:
            #TODO Validate Image
            self.image = images[0]
        self.image_count = len(images)
        self.text = experience.description[:100]
        #self.vote = experience.vote
        self.posted_by = experience.owner.firstName + " " + experience.owner.lastName


