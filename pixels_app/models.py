from django.db import models

# Create your models here.


class Profile(models.Model):
    photo = models.ImageField()
    bio = models.CharField(max_length=140)

    def __str__(self):
        return self.name

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


class Likes(models.Model):
    likes = models.IntegerField(default=0)


class Image(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=30)
    caption = models.CharField(max_length=140)
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, default=None)
    likes = models.ForeignKey(Likes, on_delete=models.CASCADE, default=None)
    comments = models.CharField(max_length=140)
    post_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-post_time']

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
