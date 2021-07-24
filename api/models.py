from django.db import models

# Create your models here.
class Album(models.Model):
    OPTIONS = (
        ('HipHop', 'HipHop'),
        ('Jazz', 'Jazz'),
        ('Classical', 'Classical'),
        ('Dance', 'Dance'),
        ('Acoustic', 'Acoustic')
    )

    title = models.CharField(max_length=120, unique=True)
    artist = models.CharField(max_length=120)
    genre = models.CharField(max_length=50, choices=OPTIONS)

    def __str__(self):
        return self.title 