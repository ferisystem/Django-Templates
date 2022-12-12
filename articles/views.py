from django.shortcuts import render
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from django.http import Http404

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
        article_obj = form.save()
        context = {
            'form': ArticleForm(),
            'created': True,
            'object': article_obj,
        }
    return render(
        request,
        "articles/create.html",
        context=context
    )


def article_detail_view(request, slug=None):
    article_obj = None
    if id is not None:
        try:
            article_obj = Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise Http404
        except:
            raise Http404
    context = {
        "object": article_obj,
    }
    return render(
        request,
        "articles/detail.html",
        context=context,
    )