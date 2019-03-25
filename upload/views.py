from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from django.http import HttpResponse
from upload import models
from django.http.response import JsonResponse
from django.shortcuts import render_to_response

import os
import json
from . import models

def result(request):
    Dict = [
                {
                    'city': 'Beijing',
                    'country': 'CHN'
                },
                {
                    'city': 'Riverside',
                    'country': 'USA'
                }
            ]
    return render(request, 'upload/result.html', {
        'Dict': json.dumps(Dict)
    })

def index(request):
    articles = models.Article.objects.all()
    return render(request, 'upload/index.html', {'articles':articles})

def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'upload/article_page.html', {'article':article})

def upload(request):
    if request.method == 'POST':# 获取对象
        obj = request.FILES.get('document')
        print(obj.name)
        print(obj.size)
    return render(request, 'upload/upload.html')
