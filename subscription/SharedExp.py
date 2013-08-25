__author__ = 'dogukansonmez'

class SharedExp:
    def __init__(self, httpRequest):
       title = httpRequest.get('title','')
       where = httpRequest.get('where','')
       when = httpRequest.get('when','')
       whitWhom = httpRequest.get('whitWhom','')
       vote = httpRequest.get('vote','')
       description = httpRequest.get('description','')

    def getExperience(self):
        return ''


