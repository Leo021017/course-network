'''
Author: Leo
Date: 2023-05-31 16:21:18
LastEditTime: 2023-05-31 20:25:09
FilePath: \network\search\models.py
Description: Leo的一些没用的代码
'''
from django.db import models

# Create your models here.
from django.db import models


class Posts(models.Model):
    post = models.CharField(max_length=255, blank=True, null=True)
    likes = models.CharField(max_length=255, blank=True, null=True)
    time = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'posts'


class Search(models.Model):
    like_list = models.TextField(blank=True, null=True)
    post_list = models.TextField(blank=True, null=True)
    time_list = models.TextField(blank=True, null=True)
    keyword = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'search'
