from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from django.http import Http404
from django.db.models import Q

# Create your views here.
def article_search_view(request):
    query_set = request.GET
    query = query_set.get('q')
    article_obj = Article.objects.search(query=query)
    print(article_obj)
    if len(article_obj) == 0:
        article_obj = {
            "title": f"{query} Article Not Exist",
            "content": f"{query} Article Not Exist",
            "id": f"{query} Article Not Exist",
        }
    context = {
        "object_list": article_obj,
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
        # return redirect("article-detail", slug=article_obj.slug) # way 1st
        return redirect(article_obj.get_absolute_url()) # better way
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
        except Article.MultipleObjectsReturned:
            article_obj = Article.objects.filter(slug=slug).first()
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