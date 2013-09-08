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
    when = models.TextField()
    withWhom= models.TextField()
    vote = models.IntegerField()
    img_links = models.TextField()
    video_links = models.TextField()
    description = models.TextField()
    postDate = models.DateTimeField(auto_now=True)
    tags = models.TextField()
    commentCount = models.IntegerField()

    def __unicode__(self):
        return self.name

class Comment(models.Model):
    name = models.TextField()
    owner = models.ForeignKey("User")
    text= models.TextField()
    experience = models.ForeignKey(Experience)
    date = models.TextField()

    def __unicode__(self):
        return self.name


