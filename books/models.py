from django.db import models
from django.shortcuts import reverse


class Book(models.Model):
    title = models.CharField(max_length=50,)
    author = models.CharField(max_length=50)
    description = models.TextField()
    date_time_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # canonical url
        return reverse('post_detail', args=[self.id])

