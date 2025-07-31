from django.db import models
from django.contrib.auth.models import AbstractUser

class AppUser(AbstractUser):
    vk_user_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    height = models.IntegerField(null=True, blank=True, default=175)
    weight = models.IntegerField(null=True, blank=True, default=70)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.username}"
