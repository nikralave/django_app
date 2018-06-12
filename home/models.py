from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(max_length=200, blank=False)
    
    def __str__(self):
        return self.name
        
class Book(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    author = models.ForeignKey(Author, null=False, related_name="books")
    
    def __str__(self):
        return self.name