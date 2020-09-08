from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Poll(models.Model):
    title = models.CharField(max_length=100)
    question = models.TextField(max_length=250)
    question_image = models.ImageField(default=None)
    time_posted = models.DateTimeField(default=timezone.now)
    #considering global polls can never be deleted by any user
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.CharField(max_length=10)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("poll-detail", kwargs={"pk": self.pk})
    
class PollChoices(models.Model):
    choice_text = models.CharField(max_length=100)
    choice_image= models.ImageField(default = None)
    choice_count = models.PositiveSmallIntegerField(default=0)
    poll = models.ForeignKey(Poll, on_delete= models.CASCADE)

