from django.urls import path
from product import views
urlpatterns = [
    
    # path("",views.view_category,name="view_all_category"),
    path("",views.CategoryList.as_view(),name="view_all_category"),
    
    
    # path("<int:pk>/",views.view_specific_category,name="specific_category"),
    path("<int:pk>/",views.SpecificCategory.as_view(),name="specific_category")
    
]
