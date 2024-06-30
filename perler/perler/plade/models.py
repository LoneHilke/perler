from django.db import models

# Create your models here.
class Plade(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    category = models.ManyToManyField('Category', related_name='item')
    kant = models.ManyToManyField('Kant', related_name='item')
    def __str__(self):
        return self.name

class Runde(models.Model):
  name = models.CharField(max_length=200)
  description = models.TextField()
  image = models.ImageField(upload_to='images/')
  category = models.ManyToManyField('Category')
  kant = models.ManyToManyField('Kant')
  def __str__(self):
      return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=200)

class Kant(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    