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
            'country': 'CHN',
            'next': 'Shijiazhuang',
            'wayToNext': 'Railway',
            'flag': 1
        },
        {
            'city': 'Shijiazhuang',
            'country': 'CHN',
            'next': 'Taiyuan',
            'wayToNext': 'Railway',
            'flag': 0,
        },
        {
            'city': 'Shijiazhuang',
            'country': 'CHN',
            'next': 'Zhengzhou',
            'wayToNext': 'Railway',
            'flag': 0,
        },
        {
            'city': 'Zhengzhou',
            'country': 'CHN',
            'next': 'None',
            'flag': 0,
        },
        {
            'city': 'Zhengzhou',
            'country': 'CHN',
            'next': 'Wuhan',
            'wayToNext': 'Railway',
            'flag': 0,
        },
        {
            'city': 'Wuhan',
            'country': 'CHN',
            'next': 'Changsha',
            'wayToNext': 'Railway',
            'flag': 0,
        },
        {
            'city': 'Wuhan',
            'country': 'CHN',
            'next': 'Chongqing',
            'wayToNext': 'Railway',
            'flag': 0,
        },
        {
            'city': 'Chongqing',
            'country': 'CHN',
            'next': 'Chengdu',
            'wayToNext': 'Railway',
            'flag': 0,
        },
        {
            'city': 'Chengdu',
            'country': 'CHN',
            'next': 'Guiyang',
            'wayToNext': 'Railway',
            'flag': 0,
        },
        {
            'city': 'Guiyang',
            'country': 'CHN',
            'next': 'Guangzhou',
            'wayToNext': 'Railway',
            'flag': 3,
        },
        {
            'city': 'Changsha',
            'country': 'CHN',
            'next': 'Guangzhou',
            'wayToNext': 'Railway',
            'flag': 0,
        },
        {
            'city': 'Guangzhou',
            'country': 'CHN',
            'next': 'None',
            'flag': 2,
        },
        {
            'city': 'Taiyuan',
            'country': 'CHN',
            'next': "Xi'an",
            'wayToNext': 'Railway',
            'flag': 0,
        },
        {
            'city': "Xi'an",
            'country': 'CHN',
            'next': 'Chengdu',
            'wayToNext': 'Railway',
            'flag': 0,
        },
        {
            'city': "Zhengzhou",
            'country': 'CHN',
            'next': "Xi'an",
            'wayToNext': 'Railway',
            'flag': 0,
        },
    ]


    Dict_ = [
        {
            'city': 'Beijing',
            'country': 'CHN',
            'next': 'Shijiazhuang',
            'wayToNext': 'Railway',
            'flag': 1,
        },
        {
            'city': 'Shijiazhuang',
            'country': 'CHN',
            'next': 'Taiyuan',
            'wayToNext': 'Railway',
            'flag': 0,
        },
        {
            'city': 'Shijiazhuang',
            'country': 'CHN',
            'next': 'Zhengzhou',
            'wayToNext': 'Railway',
            'flag': 0,
        },
        {
            'city': 'Zhengzhou',
            'country': 'CHN',
            'next': 'None',
            'flag': 0,
        },
        {
            'city': 'Zhengzhou',
            'country': 'CHN',
            'next': 'Wuhan',
            'wayToNext': 'Railway',
            'flag': 0,
        },
        {
            'city': 'Wuhan',
            'country': 'CHN',
            'next': 'Changsha',
            'wayToNext': 'Railway',
            'flag': 0,
        },
        {
            'city': 'Wuhan',
            'country': 'CHN',
            'next': 'Chongqing',
            'wayToNext': 'Railway',
            'flag': 0,
        },
        {
            'city': 'Chongqing',
            'country': 'CHN',
            'next': 'Chengdu',
            'wayToNext': 'Railway',
            'flag': 0,
        },
        {
            'city': 'Chengdu',
            'country': 'CHN',
            'next': 'Guangzhou',
            'wayToNext': 'Airplane',
            'flag': 0,
        },
        {
            'city': 'Changsha',
            'country': 'CHN',
            'next': 'Guangzhou',
            'wayToNext': 'Railway',
            'flag': 0,
        },
        {
            'city': 'Guangzhou',
            'country': 'CHN',
            'next': 'None',
            'flag': 2,
        },
        {
            'city': 'Taiyuan',
            'country': 'CHN',
            'next': "Xi'an",
            'wayToNext': 'Railway',
            'flag': 0,
        },
        {
            'city': "Xi'an",
            'country': 'CHN',
            'next': 'Chengdu',
            'wayToNext': 'Railway',
            'flag': 0,
        },
        {
            'city': "Zhengzhou",
            'country': 'CHN',
            'next': "Xi'an",
            'wayToNext': 'Railway',
            'flag': 0,
        },
    ]
    return render(request, 'upload/result.html', {
        'Dict': json.dumps(Dict),
        'Dict_': json.dumps(Dict_)
    })

def index(request):
    articles = models.Article.objects.all()
    return render(request, 'upload/index.html', {'articles':articles})

def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'upload/article_page.html', {'article':article})

def test(request):
    Dict = [
        {
            'city': 'Beijing',
            'country': 'CHN',
            'next': 'Shijiazhuang',
            'wayToNext': 'Railway'
        },
        {
            'city': 'Shijiazhuang',
            'country': 'CHN',
            'next': 'Taiyuan',
            'wayToNext': 'Railway'
        },
        {
            'city': 'Shijiazhuang',
            'country': 'CHN',
            'next': 'Zhengzhou',
            'wayToNext': 'Railway'
        },
        {
            'city': 'Zhengzhou',
            'country': 'CHN',
            'next': 'None',
        },
        {
            'city': 'Zhengzhou',
            'country': 'CHN',
            'next': 'Wuhan',
            'wayToNext': 'Railway'
        },
        {
            'city': 'Wuhan',
            'country': 'CHN',
            'next': 'Changsha',
        },
        {
            'city': 'Wuhan',
            'country': 'CHN',
            'next': 'Chongqing',
            'wayToNext': 'Railway'
        },
        {
            'city': 'Chongqing',
            'country': 'CHN',
            'next': 'Chengdu',
            'wayToNext': 'Railway'
        },
        {
            'city': 'Chengdu',
            'country': 'CHN',
            'next': 'Guiyang',
            'wayToNext': 'Railway'
        },
        {
            'city': 'Guiyang',
            'country': 'CHN',
            'next': 'Guangzhou',
            'wayToNext': 'Railway'
        },
        {
            'city': 'Changsha',
            'country': 'CHN',
            'next': 'Guangzhou',
            'wayToNext': 'Railway'
        },
        {
            'city': 'Guangzhou',
            'country': 'CHN',
            'next': 'None',
        },
        {
            'city': 'Taiyuan',
            'country': 'CHN',
            'next': "Xi'an",
            'wayToNext': 'Railway'
        },
        {
            'city': "Xi'an",
            'country': 'CHN',
            'next': 'Chengdu',
            'wayToNext': 'Railway'
        },
        {
            'city': "Zhengzhou",
            'country': 'CHN',
            'next': "Xi'an",
            'wayToNext': 'Railway'
        },
    ]

    Dict_ = [
        {
            'city': 'Beijing',
            'country': 'CHN',
            'next': 'Shijiazhuang',
            'wayToNext': 'Railway'
        },
        {
            'city': 'Shijiazhuang',
            'country': 'CHN',
            'next': 'Taiyuan',
            'wayToNext': 'Railway'
        },
        {
            'city': 'Shijiazhuang',
            'country': 'CHN',
            'next': 'Zhengzhou',
            'wayToNext': 'Railway'
        },
        {
            'city': 'Zhengzhou',
            'country': 'CHN',
            'next': 'None',
        },
        {
            'city': 'Zhengzhou',
            'country': 'CHN',
            'next': 'Wuhan',
            'wayToNext': 'Railway'
        },
        {
            'city': 'Wuhan',
            'country': 'CHN',
            'next': 'Changsha',
        },
        {
            'city': 'Wuhan',
            'country': 'CHN',
            'next': 'Chongqing',
            'wayToNext': 'Railway'
        },
        {
            'city': 'Chongqing',
            'country': 'CHN',
            'next': 'Chengdu',
            'wayToNext': 'Railway'
        },
        {
            'city': 'Chengdu',
            'country': 'CHN',
            'next': 'Guangzhou',
            'wayToNext': 'Airplane'
        },
        {
            'city': 'Changsha',
            'country': 'CHN',
            'next': 'Guangzhou',
            'wayToNext': 'Railway'
        },
        {
            'city': 'Guangzhou',
            'country': 'CHN',
            'next': 'None',
        },
        {
            'city': 'Taiyuan',
            'country': 'CHN',
            'next': "Xi'an",
            'wayToNext': 'Railway'
        },
        {
            'city': "Xi'an",
            'country': 'CHN',
            'next': 'Chengdu',
            'wayToNext': 'Railway'
        },
        {
            'city': "Zhengzhou",
            'country': 'CHN',
            'next': "Xi'an",
            'wayToNext': 'Railway'
        },
    ]


    return render(request, 'upload/test.html', {'Dict': json.dumps(Dict), 'Dict_':json.dumps(Dict_)})

def upload(request):
    if request.method == 'POST':# 获取对象
        obj1 = request.FILES.get('document1')
        print(obj1.name)
        print(obj1.size)
        obj2 = request.FILES.get('document2')
        print(obj2.name)
        print(obj2.size)
    return render(request, 'upload/upload.html')
