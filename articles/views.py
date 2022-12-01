from django.shortcuts import render
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm

# Create your views here.
def article_search_view(request):
    query_set = request.GET
    query = query_set.get('q')
    article_obj = None
    if query is not None:
        try:
            article_obj = Article.objects.get(id=int(query))
        except:
            article_obj = {
                "title": f"{query} Article Not Exist",
                "content": f"{query} Article Not Exist",
                "id": f"{query} Article Not Exist",
            }
    context = {
        "object": article_obj,
    }
    return render(
        request,
        "articles/search.html",
        context=context,
    )


@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    context = {
        "form": form,
    }
    if form.is_valid():
        title = form.cleaned_data.get("title")
        content = form.cleaned_data.get("content")
        article_obj = Article.objects.create(
            title = title,
            content = content,
        )
        context = {
            'object': article_obj,
            'created': True,
        }
    return render(
        request,
        "articles/create.html",
        context=context
    )


def article_detail_view(request, id=None):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)
    context = {
        "object": article_obj,
    }
    return render(
        request,
        "articles/detail.html",
        context=context,
    )