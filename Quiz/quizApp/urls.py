from django.contrib import admin
from django.urls import path, include
from .views import Quiz, RandomQuestion, QuizQuestion
urlpatterns = [
    path('', Quiz.as_view(), name='quiz'),
    path('random/<str:topic>/', RandomQuestion.as_view(), name='RandomQuestion'),
    path('quiz/<str:topic>/', QuizQuestion.as_view(), name='QuizQuestion')
]
