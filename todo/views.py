from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#main index page
def index(request):
    return HttpResponse("Hello, world. You're at the todo app index.")
    #note to self - ^HttpResponse is not equivalent to HTTPResponse!