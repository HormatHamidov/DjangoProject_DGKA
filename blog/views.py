from django.shortcuts import render
from blog.models import Article
# Create your views here.

def home_page(request):
    return render(request, "index.html")


def about_page(request):
    articles = Article.objects.all()
    context = {
        "articles": articles,
    }
    return render(request, "about.html", context)


def contact_page(request):
    return render(request, "contact.html")