from django.db import models


class Timeline(models.Model):

    user = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)