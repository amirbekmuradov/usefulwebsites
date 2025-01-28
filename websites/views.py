from django.shortcuts import render, redirect, get_object_or_404
from .models import Website, Like, Comment
from .forms import WebsiteForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.http import JsonResponse

def home(request):
    query = request.GET.get('q', '')
    sort_by = request.GET.get('sort', 'created_at')

    websites = Website.objects.filter(title__icontains=query).order_by(f'-{sort_by}')

    user_likes = set()
    if request.user.is_authenticated:
        user_likes = set(Like.objects.filter(user=request.user).values_list('website_id', flat=True))
    
    for website in websites:
        website.is_liked = website.id in user_likes

    return render(request, 'websites/home.html', {
        'websites': websites, 
        'current_sort': sort_by, 
        'query': query,
        'user_likes': user_likes
    })


def add_website(request):
    if request.method == 'POST':
        form = WebsiteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Website added successfully!')
            return redirect('/')
    else:
        form = WebsiteForm()

    return render(request, 'websites/add_website.html', {'form': form})


@login_required
def profile(request):
    liked_websites = Website.objects.filter(like__user=request.user)
    comments = Comment.objects.filter(user=request.user)
    return render(request, 'websites/profile.html', {
        'liked_websites': liked_websites, 
        'comments': comments
    })


@login_required
def like_website(request, website_id):
    if request.method == "POST":  # Only handle POST requests
        website = get_object_or_404(Website, id=website_id)
        liked = False  # Track if user liked or unliked

        # Check if the user already liked the website
        existing_like = Like.objects.filter(user=request.user, website=website)
        if existing_like.exists():
            # User is unliking the website
            existing_like.delete()
            website.likes -= 1
        else:
            # User is liking the website
            Like.objects.create(user=request.user, website=website)
            website.likes += 1
            liked = True

        website.save()  # Save the updated like count
        return JsonResponse({"liked": liked, "likes": website.likes})  # JSON response

    # Return error for non-POST requests
    return JsonResponse({"error": "Invalid request"}, status=400)


@login_required
def add_comment(request, website_id):
    website = get_object_or_404(Website, id=website_id)
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            Comment.objects.create(user=request.user, website=website, text=text)
    return redirect('/')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Signup successful!')
            return redirect('/')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})
