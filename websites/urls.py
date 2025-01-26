from django.contrib import admin
from django.urls import path, include
from websites import views

urlpatterns = [
    
    path('', views.home, name='home'),  # Home page
    path('signup/', views.signup, name='signup'),  # Signup page
    path('like/<int:website_id>/', views.like_website, name='like_website'),  # Like/unlike functionality
    path('comment/<int:website_id>/', views.add_comment, name='add_comment'),
    path('add/', views.add_website, name='add_website'),  # Add a new website
    path('accounts/', include('django.contrib.auth.urls')),  # Built-in auth views (login, logout, etc.)
    path('profile/', views.profile, name='profile'),
]
