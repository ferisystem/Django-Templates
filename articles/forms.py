from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content"]
    
    def clean(self):
        data = self.cleaned_data
        title = data.get("title")
        content = data.get("content")
        qs = Article.objects.filter(title__icontains=title)
        qs2 = Article.objects.filter(content__icontains=content)
        if qs.exists():
            self.add_error("title", f"\"{title}\" already taken! use another one.")
        if qs2.exists():
            self.add_error("title", f"\"{content}\" already taken! use another one.")
        return data


class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if title.lower().strip() == "the office":
            self.add_error('title', 'This title is taked.')
        if 'office' in content:
            self.add_error("content", "Office cann't be in content")
        return cleaned_data