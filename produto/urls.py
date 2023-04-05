from rest_framework_nested import routers
from django.urls import include, path

router = routers.SimpleRouter()
router.register(r'bolsas', DomainViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
]
