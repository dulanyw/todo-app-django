from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

#main index page
def index(request):
    return HttpResponse("Hello, world. You're at the todo app index.")
    #note to self - ^HttpResponse is not equivalent to HTTPResponse!

# ***Topics views***
# create a new topic
class TopicCreate(generic.CreateView):
    model = Topic
    template_name = 'todo/topic_form.html'

# edit a topic
class TopicEdit(generic.UpdateView):
    model = Topic
    template_name = 'todo/topic_form.html'


# ***TodoItem views***
# view details of a single todo item
class TodoDetail(generic.DetailView):
    model = TodoItem
    template_name = 'todo/todo_detail.html'

# create a new todo item
class TodoCreate(generic.CreateView):
    model = TodoItem
    template_name = 'todo/todo_form.html'

# update a todo item
class TodoEdit(generic.UpdateView):
    model = TodoItem
    template_name = 'todo/todo_form.html'

