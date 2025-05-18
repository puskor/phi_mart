from django.urls import path
from product import views
urlpatterns = [
    path("",views.view_product,name="view_all_product"),
    path("<int:id>/",views.view_specific_product,name="specific_product"),
]
