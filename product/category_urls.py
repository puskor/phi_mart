from django.urls import path
from product import views
urlpatterns = [
    
    path("",views.view_category),
    path("view_specific_category/<int:pk>/",views.view_specific_category,name="specific_category")
]
