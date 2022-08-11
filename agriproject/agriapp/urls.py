
from django.urls import path,include
from . import views
app_name='agriapp'
urlpatterns = [

    path('',views.index,name='index'),
    path('agri/<int:agri_id>/',views.detail,name='detail'),
    path('add/',views.add_agri,name='add_agri'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
]
