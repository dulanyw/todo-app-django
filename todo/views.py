from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#main index page
def index(request):
    return HttpResponse("Hello, world. You're at the todo app index.")
    #note to self - ^HttpResponse is not equivalent to HTTPResponse!

# ***Topics views***
# create a new topic
def topic_create(request):
    pass

# update a topic
def topic_update(request, topic_id):
    pass


# ***TodoItem views***
# view details of a single todo item
def todo_detail(request, todo_id):
    pass

# create a new todo item
def todo_create(request):
    pass

# update a todo item
def todo_update(request, todo_id):
    pass

