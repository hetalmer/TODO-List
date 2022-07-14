from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='home-page'),
    path('edit/<int:slug>',views.edit,name='edit-page'),
    path('delete/<int:slug>',views.delete,name='delete-page')
]
