from django.db import models


class Feed(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField(unique=True, db_index=True)
    base_link = models.ForeignKey('BaseLinks', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' ' + self.base_link.name


class BaseLinks(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='base_images/', blank=True, null=True)
    base_link = models.URLField(unique=True, db_index=True)
