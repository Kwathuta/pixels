from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    photo = models.ImageField(upload_to='pixels/')
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=140, blank=True)

    def __str__(self):
        return self.username

    def save_profile(self):
        self.save()

    def update_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profile_by_username(cls, username):
        profile = cls.objects.filter(username=username)
        return profile


class Image(models.Model):
    image = models.ImageField(upload_to='pixels/')
    name = models.CharField(max_length=30)
    caption = models.CharField(max_length=140)
    profile = models.ForeignKey(
        User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="images")
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

    def update_caption(self, new_caption):
        self.caption = new_caption
        self.save()

    @classmethod
    def get_images_by_user(cls, user):
        images = cls.objects.filter(user=user)
        return images

    @classmethod
    def search_by_image_name(cls, search_term):
        images = cls.objects.filter(name__icontains=search_term)
        return images

    @classmethod
    def get_image(cls, id):
        image = cls.objects.get(id=id)
        return image
