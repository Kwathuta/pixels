from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    photo = models.ImageField()
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=140)

    def __str__(self):
        return self.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


class Image(models.Model):
    image = models.ImageField(upload_to='pixels/')
    name = models.CharField(max_length=30)
    caption = models.CharField(max_length=140)
    profile = models.ForeignKey(
        User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    comments = models.IntegerField(default=0)
    post_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-post_time']

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
