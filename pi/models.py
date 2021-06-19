from django.db import models

# Create your models here.


class Temperature(models.Model):
    title = models.CharField(max_length=32, default='')

    def __str__(self):
        return self.title
