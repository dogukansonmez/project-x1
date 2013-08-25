__author__ = 'dogukansonmez'

class ExpItem:
    id = ""
    type = ""
    title = ""
    tags = ""
    postDate = ""
    image = ""
    video = ""
    text = ""
    numberOfComments= 0

    def __init__(self, experience):
        ExpItem.id = experience.id
        ExpItem.type = experience.type
        ExpItem.title = experience.title
        ExpItem.tags = experience.tags
        ExpItem.postDate = experience.postDate
        ExpItem.image = experience.img_links
        ExpItem.video =experience.video_links
        ExpItem.text = experience.description[:100]
        ExpItem.numberOfComments = experience.commentCount


