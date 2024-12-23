from django.db import models

class Category(models.Model):
  nome = models.CharField(max_length=50)

  def __str__ (self):
    return self.nome

class Livros (models.Model):
  streaming_choices = (('AK', 'Amazon Kindle'), ('F', 'Físico'))
  name = models.CharField(max_length=50)
  streaming = models.CharField(max_length=2, choices=streaming_choices)
  notice = models.IntegerField(null=True, blank=True)
  coments = models.TextField(null=True, blank=True)
  category = models.ManyToManyField(Category) 

  def __str__ (self):
    return self.name