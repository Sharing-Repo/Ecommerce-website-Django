from django.urls import path
from home import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='index'),
    path('userform/', views.form, name='form'),
    path('djangoform/', views.djangoForm, name="djangoform"),
    path('modelform', views.ModelsForm, name='modelform'),
    
    path('<int:item_ID>/', views.details, name="details"),
    path('updatepage/<int:item_ID>', views.UpdateForm, name='updateform'),

    path('imgform/', views.imageform, name='imgform'),
    path('allimage/',  views.allImage, name='allimage'),
]