from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Image, Profile, Likes, Comments

# Create your views here.


@login_required(login_url='/accounts/login/')
def index(request):
    '''
    get all the images from the database and order them by the date they were created
    '''
    images = Image.objects.all().order_by('-post_time')
    return render(request, 'index.html', {'images': images})


@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    # get images for the current logged in user
    images = Image.objects.filter(user_id=current_user.id)
    # get the profile of the current logged in user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    return render(request, 'profile.html', {"images": images, "profile": profile})
    # return render(request, 'profile.html')


@login_required(login_url='/accounts/login/')
def like_image(request, id):
    likes = Likes.objects.filter(image_id=id).first()
    # check if the user has already liked the image
    if Likes.objects.filter(image_id=id, user_id=request.user.id).exists():
        # unlike the image
        likes.delete()
        # reduce the number of likes by 1 for the image
        image = Image.objects.get(id=id)
        # check if the image like_count is equal to 0
        if image.likes == 0:
            image.likes = 0
            image.save()
        else:
            image.likes -= 1
            image.save()
        return redirect('/')
    else:
        likes = Likes(image_id=id, user_id=request.user.id)
        likes.save()
        # increase the number of likes by 1 for the image
        image = Image.objects.get(id=id)
        image.likes = image.likes + 1
        image.save()
        return redirect('/')
