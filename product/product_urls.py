from django.urls import path
from product import views
urlpatterns = [
    # path("",views.view_product,name="view_all_product"),
    # path("",views.ViewProduct.as_view(),name="view_all_product"),
    path("",views.ProductViewset.as_view(),name="view_all_product"),
    
    
    # path("<int:id>/",views.view_specific_product,name="specific_product"),
    path("<int:pk>/",views.SpecificProduct.as_view(),name="specific_product"),
    
]
