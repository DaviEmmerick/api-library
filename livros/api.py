from ninja import Router, Query
from .schemas import LivrosSchema, Avaliation_Schema, Random_Filter
from .models import Livros, Category

livros_router = Router()

@livros_router.post('/')
def create_livro(request, livro_schema: LivrosSchema):
  name = livro_schema.dict()['name']
  streaming = livro_schema.dict()['streaming']
  category = livro_schema.dict()['category']
  if streaming not in ['F', 'K']:
    return 400, {'status': 'Streaming deve ser F ou AK'}
  
  livro = Livros (
    name = name,
    streaming = streaming
  )
  livro.save()
  for categoria in category:
      categoria_temp =  Category.objects.get(id=categoria) 
      livro.category.add(categoria_temp)

  return {'status':'ok'}

@livros_router.put('/{livro_id}')
def avaliation(request, livro_id: int, avaliation_schema: Avaliation_Schema):
    coments = avaliation_schema.dict()['coments']
    notice = avaliation_schema.dict()['notice']

    try:
        livro = Livros.objects.get(id=livro_id)
    except Livros.DoesNotExist:
        return 404, {'status': 'Livro não encontrado'}

    livro.coments = coments
    livro.notice = notice
    livro.save()

    return 200, {'status': 'Avaliação realizada com sucesso'}


@livros_router.delete('/{livro_id}')
def delete_livro(request, livro_id: int):
   livro = Livros.objects.get(id=livro_id)
   livro.delete()
   return livro_id 

@livros_router.get('/random/', response={200 : LivrosSchema, 404 : dict})
def random_livro(request, filter: Query[Random_Filter]):
   nota_minima = filter.dict()['nota_minima']
   category = filter.dict()['category']
   reler = filter.dict()['reler']

   livros = Livros.objects.all()
   if not reler:
      livros = livros.filter(notice=None)  

   if nota_minima:
      livros = livros.filter(notice__gte=nota_minima)

   if category:
      livros = livros.filter(category__id=category)

   livro = Livros.order_by('?').first()
   if livro:
      return 200, livro
   else:
      return 404, {'status': 'Livro não encontrado'}  