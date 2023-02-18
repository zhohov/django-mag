from django.db import models
from django.urls import reverse


class Article(models.Model):
    image = models.ImageField(upload_to='image/', null=True)
    title = models.CharField('title', max_length=100, null=False)
    description = models.TextField('description', max_length=250, null=False)
    text = models.TextField('text', null=False)
    date = models.DateTimeField('date')
    number = models.IntegerField('number', default=1)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('release-detail', kwargs={'pk': self.pk})


class Release(models.Model):
    image = models.ImageField(upload_to='image/', null=True)
    title = models.CharField('title', max_length=100, null=False)
    description = models.TextField('description', max_length=250, null=False)
    text = models.TextField('text', default="текст", null=False)
    number = models.IntegerField('number', null=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('release-detail', kwargs={'pk': self.pk})
