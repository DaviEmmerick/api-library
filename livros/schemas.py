from ninja import ModelSchema, Schema
from .models import Livros

class LivrosSchema(ModelSchema):
  class Meta:
    model = Livros
    fields = ['name', 'streaming', 'category']
    
class Avaliation_Schema(ModelSchema):
  class Meta:
    model = Livros
    fields = ['notice', 'coments']

class Random_Filter(Schema):
  nota_minima: int = None
  category: int = None
  reler: bool = False 
