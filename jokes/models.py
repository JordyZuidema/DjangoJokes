from django.db import models
from django.urls import reverse

class Joke(models.Model):
    question = models.TextField(max_length=200)
    answer = models.TextField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # adding a get_absolute_url method to have a dynamic way to get the url.
    def get_absolute_url(self):
        return reverse("jokes:detail", args=[str(self.pk)])
    


    def __str__(self):
        return self.question


        