"""
To render html web pages
"""
from django.http import HttpResponse
from articles.models import Article
import random


def home_view(request):
    """
    Take in a request (Django sends request)
    Return HTML as a response (We pick to return the response)
    """
    name = "Alireza"
    random_id = random.randint(1, 4)
    
    # from database
    article_obj = Article.objects.get(id=random_id)
    article_title = article_obj.title
    article_content = article_obj.content
    
    H1_STRING = f"""
    <h1>{article_title} (id: {article_obj.id})!</h1>
    """
    P_STRING = f"""
    <p>{article_content}!</p>
    """
    HTML_STRING = H1_STRING + P_STRING
    return HttpResponse(HTML_STRING)