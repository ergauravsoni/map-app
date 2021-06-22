from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('india_map', views.india_map, name='india_map'),
    path('india_map/puzzle', views.puzzle, name='puzzle'),
    path('kt', views.kt, name='kt'),
    path('quiz', views.quiz, name='quiz'),
]
