from rest_framework.viewsets import ModelViewSet

from produto.models import Produtos 
from produto.serializers import ProdutosSerializer


class ProdutosViewSet(ModelViewSet):
    queryset = Produtos.objects.all()
    serializer_class = ProdutosSerializer
