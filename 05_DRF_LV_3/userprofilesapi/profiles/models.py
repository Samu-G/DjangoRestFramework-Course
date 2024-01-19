from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=240, blank=True)
    city = models.CharField(max_length=30, blank=True)
    avatar = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user}'s profile"
    
class ProfileStatus(models.Model):
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    status_content = models.CharField(max_length=240, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'statuses'
    
    def __str__(self):
        return f"{self.user_profile}"
