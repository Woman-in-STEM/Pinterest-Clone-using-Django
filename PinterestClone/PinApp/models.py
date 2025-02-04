from django.contrib.auth.models import User
from django.db import models


class Board(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="boards")

    def __str__(self):
        return self.name


class Pin(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="pins/")
    description = models.TextField(blank=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name="pins")

    def __str__(self):
        return self.title
