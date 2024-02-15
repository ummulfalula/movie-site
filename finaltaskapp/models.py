from django.db import models

# Create your models here.

# class Category(models.Model):
#     name=models.CharField(max_length=250)
#     def __str__(self):
#         return self.name
class Movies(models.Model):
    movie_title=models.CharField(max_length=250)
    poster_img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    release_date=models.DateField()
    actors=models.CharField(max_length=250)
    category=models.CharField(max_length=250)
    ylink=models.URLField(max_length=200)
    def __str__(self):
        return self.movie_title

