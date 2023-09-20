'''
Author: Leo
Date: 2023-05-31 16:21:18
LastEditTime: 2023-06-27 16:20:53
FilePath: \network\search\views.py
Description: Leo的一些没用的代码
'''
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from search.models import Search

import subprocess


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    # template = loader.get_template('search/index.html')
    # return HttpResponse(template.render(request))
    myword = request.POST.get("aa")
    if myword:
        print(myword)
        fp = open('D:/Python/workspace_pycharm/network/damus/damus/spiders/word.txt', 'w', encoding='utf-8')
        fp.write(myword)
        # 指定目录路径
        path = r'D:/Python/workspace_pycharm/network/damus/damus'

        # 要执行的命令
        cmd = 'scrapy crawl test'

        # 在指定目录下执行命令
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=path)
    return render(request, 'search/index.html')

    

def get_queryset(request):
    keyword = request.POST.get("keyword")
    print(keyword)
    if keyword:
        content = Search.objects.all().filter(keyword=keyword)
        for i in content:
            print(i.post_list)
        context = {'context': content}
        print(content)
        return render(request, 'search/list.html',context=context)
    else:
        return render(request, 'search/list.html')


# def get_queryset(self):
#     # 题目数量
#     keyword = self.POST.query_params.get("keyword", 1)
#     #
#     if keyword:
#         self.queryset = Search.objects.all().filter(keyword=keyword)
#         return self.queryset
    # if choice_number:
    #     self.queryset = Choice.objects.all().filter(level=level).order_by('?')[:choice_number]
    # return self.queryset




