from django.shortcuts import render
from .models import Article
import openai
from django.conf import settings
from django.shortcuts import render

openai.api_key = settings.OPENAI_API_KEY

def chatbot(request):
    response = None
    if request.method == "POST":
        question = request.POST.get('question')
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=question,
            max_tokens=150
        )
        response = response.choices[0].text.strip()
    return render(request, 'main/chatbot.html', {'response': response})

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'main/article_list.html', {'articles': articles})
# Create your views here.
