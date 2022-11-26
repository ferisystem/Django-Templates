"""
To render html web pages
"""
from django.http import HttpResponse
from articles.models import Article
from django.template.loader import render_to_string
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
    article_querysets = Article.objects.all()
    context = {
        "object_list": article_querysets,
        "object": article_obj,
        "id": article_obj.id,
        "title": article_title,
        "content": article_content,
    }

    # Django Templates
    HTML_STRING = render_to_string(
        "home-view.html",
        context=context,
    )
    # HTML_STRING = """
    # <h1>{title} (id: {id})!</h1>
    # <p>{content}!</p>
    # """.format(**context)
    return HttpResponse(HTML_STRING)