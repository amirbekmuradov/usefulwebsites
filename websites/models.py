from django.db import models
from django.contrib.auth.models import User

class Website(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    description = models.TextField()
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    website = models.ForeignKey(Website, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'website')

    def __str__(self):
        return f"{self.user.username} liked {self.website.title}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} commented on {self.website.title}"