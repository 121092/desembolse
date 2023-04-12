from rest_framework_nested import routers
from django.urls import include, path

from produto.viewsets import ProdutosViewSet


router = routers.SimpleRouter()
router.register(r'produtos', ProdutosViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
]
