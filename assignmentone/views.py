from django.shortcuts import render


__author__ = 'Mehdi Nuruzade'

from django.http import HttpResponse
import datetime
from django.http import Http404
from django.template.loader import get_template
from django.template import Context
def count(request):
    word_list=[]
    file = open('/Users/mixaylo/PycharmProjects/untitled1/untitled1/data.txt', 'r')
    for line in file:
        for word in line.split():
            word_list.append(word)
    word_dict={}
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word]=1

    a=get_template("result.html")
    html=a.render(Context({"list":word_dict}))
    return HttpResponse(html)

