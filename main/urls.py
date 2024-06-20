from django.urls import path
from .views import article_list
from .views import chatbot

urlpatterns = [
    path('chatbot/', chatbot, name='chatbot'),
]

urlpatterns = [
    path('', article_list, name='article_list'),
]
