from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.
class Ebook(models.Model):
    title = models.CharField(max_length=140)
    author = models.CharField(max_length=60)
    description = models.TextField()
    pubblication_date = models.DateField()

    def __str__(self):
        return f"{self.title} by {self.author}"

class Review(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    review = models.TextField(blank=True, null=True)
    review_author = models.CharField(max_length=8, blank=True, null=True)

    ebook = models.ForeignKey(Ebook, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f"{self.rating} by {self.review_author} for {self.ebook}"