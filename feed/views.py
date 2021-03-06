from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from feed.forms import PostForm
from feed.models import Posts, Comments
from main.models import Restaurant
from user.models import CustomUser, Follows


@login_required()
def feed(request):
    user = CustomUser.objects.get(username=request.user.username)
    following = Follows.objects.filter(follower=user).count()
    followers = Follows.objects.filter(following=user).count()
    post_list = Posts.objects.order_by('-posted_date')[:5]
    restaurants = Restaurant.objects.all()
    post_form = PostForm()
    return render(request, 'feed.html',
                  {'user': user, 'following': following, 'followers': followers, 'post_list': post_list,
                   'restaurants': restaurants, 'post_form': post_form})


@login_required()
def comment(request):
    if request.method == 'POST':
        post = Posts.objects.get(post_id=request.POST['post_id'])
        body = request.POST['body']

        com = Comments(post=post, body=body, user=request.user)
        com.save()
        messages.success(request, "Your comment has been added")
        return redirect('Feed:Feed')


@login_required()
def post(request):
    if request.method == 'POST':
        post_data = PostForm(request.POST, request.FILES)
        if post_data.is_valid():
            pos = post_data.save(commit=False)
            pos.user = request.user
            pos.save()
            messages.success(request, "Your post has been uploaded")
            return redirect('Feed:Feed')
        else:
            messages.error(request, "There is an error in the post, please try again")
            return redirect('Feed:Feed')


@login_required()
def follow_view(request, **kwargs):
    following = CustomUser.objects.get(account_id=kwargs['following_id'])
    follower = request.user
    if following == follower:
        messages.error(request, "You cannot follow yourself")
        return redirect('Feed:Feed')

    fol = Follows(following=following, follower=follower)
    fol.save()
    messages.success(request, f"You are now following {following.username}")
    return redirect('Feed:Feed')


@login_required()
def like_view(request):
    post = Posts.objects.get(post_id=request.POST['post_id'])
    post.likes += 1
    post.save()
    messages.success(request, "You liked a post")
    return redirect('Feed:Feed')
