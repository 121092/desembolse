from rest_framework.serializers import ModelSerializer

from produto.models import Produtos

class ProdutosSerializer(ModelSerializer):
    class Meta:
        model = Produtos
        fields = ["id", "nome", "valor"]