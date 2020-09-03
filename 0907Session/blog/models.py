from django.db import models


class Hashtag(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    hashtag=models.ManyToManyField(Hashtag)

    def __str__(self):
        return self.title

    # def summary(self):
    #     return self.body[:100]