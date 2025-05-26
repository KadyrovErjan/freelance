from django.db import models
from django.contrib.auth.models import AbstractUser


class Skills(models.Model):
    skills = models.CharField(max_length=42)

    def __str__(self):
        return self.skills

USER_ROLE = (
    ('freelancer', 'freelancer'),
    ('client', 'client')
)

class UserProfile(AbstractUser):
    role = models.CharField(max_length=10, choices=USER_ROLE, default='client')
    bio = models.TextField(null=True, blank=True)
    avatar = models.ImageField(upload_to='profile_avatar/')
    skills = models.ManyToManyField(Skills)
    social_links = models.URLField()


    def __str__(self):
        return self.username



class Category(models.Model):
    category_name = models.CharField(max_length=32)

    def __str__(self):
        return self.category_name

class Project(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    deadline = models.DateTimeField()
    STATUS_CHOICES = (
        ('open', 'open'),
        ('in_progress', 'in_progress'),
        ('completed', 'completed'),
        ('cancelled', 'cancelled')
    )
    status = models.CharField(max_length=32, choices=STATUS_CHOICES)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    skills_required = models.ManyToManyField(Skills)
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.client}, {self.title}'

class Offer(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    freelancer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    message = models.TextField(null=True, blank=True)
    proposed_budget = models.DecimalField(max_digits=10, decimal_places=2)
    proposed_deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.freelancer}'

class Review(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='client_review')
    target = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='review_target')
    rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)], null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.reviewer} - {self.rating}'


