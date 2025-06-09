import copy

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

QUESTIONS = [
    {
        'title': f'Title {i}',
        'id': i,
        'text': f'This is text for question #{i}',
        'img_path': '/img/dreamcar.jpg'
    } for i in range(30)
]

ANSWERS = [
    {
        'id': i,
        'text': f'Text for answer #{i}',
        'img_path': '/img/dreamcar.jpg'
    } for i in range(30)
]

TAGS = [
    {
        'id': i,
        'name': f'Tag {i}'
    } for i in range(5)
]

def index(request):
    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(QUESTIONS, 5)
    page = paginator.page(page_num)
    return render(request, 'index.html', context={'questions': page.object_list, 'page_obj': page, 'tags': TAGS})
def hot(request):
    q = list(reversed(copy.deepcopy(QUESTIONS)))
    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(q, 5)
    page = paginator.page(page_num)
    return render(request, 'hot.html', context={'questions': page.object_list, 'page_obj': page, 'tags': TAGS})
def signup(request):
    return render(request, 'signup.html', context={'tags': TAGS})
def login(request):
    return render(request, 'login.html', context={'tags': TAGS})
def question(request, question_id):
    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(ANSWERS, 5)
    page = paginator.page(page_num)
    return render(request, 'question.html', context={'question': QUESTIONS[question_id], 'page_obj': page, 'tags': TAGS, 'answers': page.object_list})
def ask(request):
    return render(request, 'ask.html', context={'tags': TAGS})
def settings(request):
    return render(request, 'settings.html', context={'tags': TAGS})
def tag(request, tag_id):
    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(QUESTIONS, 5)
    page = paginator.page(page_num)
    return render(request, 'tag.html', context={'questions': page.object_list, 'page_obj': page, 'tags': TAGS, 'tag': TAGS[tag_id]})