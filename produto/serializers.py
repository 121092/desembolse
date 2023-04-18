from rest_framework.serializers import ModelSerializer, ValidationError

from produto.models import Produtos

class ProdutosSerializer(ModelSerializer):
    class Meta:
        model = Produtos
        fields = ["id", "nome", "valor", "disponivel"]
    
    
    def create(self, validated_data):
        produto = Produtos(
            nome=validated_data["nome"], 
            valor=validated_data["valor"], 
            disponivel=validated_data["disponivel"]
        )
        produto.save()
        return produto


#Se comecar com a letra maiusca retornar nome, caso nao retorna falso
#Verificar se o nome ja existe, caso nao, que retorne falso

    def validate_nome(self, nome):
        if nome[0] == nome[0].title():
            pass
        else:
            nome = nome.title()
        if Produtos.objects.filter(nome= nome):
            raise ValidationError("Já cadastrado!")
        else:
            return nome


#O valor nao pode ser negativo, se for, retornar o int 0

    def validate_valor(self,valor):
        if valor > 0:
            return valor
        else:
            return 0


