from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
# Create your models here.

class Poll(models.Model):
    title = models.CharField(max_length=100)
    question = models.CharField(max_length=250)
    question_image = models.ImageField(default=None, blank = True, upload_to='question_image')
    time_posted = models.DateTimeField(default=timezone.now)
    #considering global polls can never be deleted by any user
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.CharField(max_length=10)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("poll-detail", kwargs={"link": self.link})
    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.question_image.path)
        output_size = (300,300)
        if img.height > 300 or img.width > 300:
            img.thumbnail(output_size)
            img.save(self.question_image.path)
    
class Choice(models.Model):
    choice_text = models.CharField(max_length=100)
    choice_image= models.ImageField(default = None, blank = True)
    choice_count = models.PositiveSmallIntegerField(default=0)
    poll = models.ForeignKey(Poll, on_delete= models.CASCADE)

    def __str__(self):
        return self.choice_text

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.choice_image.path)
        output_size = (150,150)
        if img.height > 150 or img.width > 150:
            img.thumbnail(output_size)
            img.save(self.choice_image.path)

