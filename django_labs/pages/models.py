from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    country = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Book(models.Model):
    year = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    title = models.TextField(max_length=100)
    synopsis = models.TextField(max_length=500)
    category = models.CharField(max_length=40, default="horror")
    def __str__(self):
        return self.title

