from django.shortcuts import render

# Create your views here.


def blog_page(reguest):
    return render(reguest, 'all_blogs.html',{})