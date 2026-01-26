from django.db import models

# Create your models here.
class Books(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.DateField()
    author = models.TextField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    title = models.TextField(max_length=100)
    synopsis = models.TextField(max_length=500)
