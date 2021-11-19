from django.urls import path 
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('resumo_da_experiencia/', views.resumo_experiencia, name='resumo'), 
    path('experiencia_profissional/', views.experiencia_profissional, name='profissional'),
    path('cursos_complementares/', views.cursos_complementares, name='cursos'),
    path('habilidades_tecnicas/', views.habilidades_tecnicas, name='habilidades'),
]

