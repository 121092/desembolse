from rest_framework.viewsets import ModelViewSet

from produto.models import Produtos 
from produto.serializers import ProdutosSerializer


#Queryset universo de objetos de um tabela manipulados por uma requisição. 
#Serializer transforma clarro/objeto na linguagem json.

class ProdutosViewSet(ModelViewSet):
    queryset = Produtos.objects.filter(disponivel=True)
    serializer_class = ProdutosSerializer
