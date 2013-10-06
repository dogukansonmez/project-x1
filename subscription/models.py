from django.db import models

class User(models.Model):
    userID = models.TextField()
    firstName = models.TextField()
    lastName = models.TextField()

class Experience(models.Model):
    name = models.TextField()
    owner = models.ForeignKey("User")
    type = models.TextField()
    title = models.TextField()
    where = models.TextField()
    when = models.DateTimeField()
    withWhom= models.TextField()
    vote = models.IntegerField()
    img_links = models.TextField()
    video_links = models.TextField()
    description = models.TextField()
    postDate = models.DateTimeField(auto_now=True)
    tags = models.TextField()

    def __unicode__(self):
        return self.name




