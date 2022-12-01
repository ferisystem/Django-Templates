from django import forms

class ArticleForm(forms.Form):
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