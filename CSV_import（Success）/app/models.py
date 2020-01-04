from django.db import models


class Post(models.Model):

    title =  models.CharField('タイトル', max_length=50)
    title1 = models.CharField('A', max_length=50)
    title2 = models.CharField('B', max_length=50)
    title3 = models.CharField('C', max_length=50)

    def __str__(self):
        return self.title


