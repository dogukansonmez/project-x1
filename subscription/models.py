from django.db import models

class Experience(models.Model):
    name = models.TextField()
    owner = models.TextField()
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
    owner = models.TextField()
    text= models.TextField()
    experience = models.ForeignKey(Experience)
    date = models.TextField()

    def __unicode__(self):
        return self.name

class Image(models.Model):
    title = models.CharField(max_length=60, blank=True, null=True)
    image = models.FileField(upload_to="images/")

    def __unicode__(self):
        return self.image.name

