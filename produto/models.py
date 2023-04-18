from django.db import models

# Create your models here.

class Produtos(models.Model):
    nome = models.CharField(max_length=50)
    valor = models.IntegerField()
    disponivel = models.BooleanField(default=True)

    #colocar atributos e fazer alteração no arquivo serializers
    #salvar(quando executar o comando makemigrations vai gerar um novo migration)


#add um novo atributo ao produto e a funcao tem que dizer a disponibilidade do produto. 
#retornar somente oos produtos disponiveis na listagem de produtos.
