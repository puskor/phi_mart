from django.urls import path,include
from rest_framework.routers import DefaultRouter
from product.views import ProductViewset,CategoryViewset

router= DefaultRouter()
router.register("products",ProductViewset)
router.register("categorys",CategoryViewset)


urlpatterns = [
    path("",include(router.urls)),
]


