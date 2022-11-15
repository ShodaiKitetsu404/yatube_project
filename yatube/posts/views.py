from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def group(request):
    return HttpResponse('Список групп')


def group_posts(request, slug):
    return HttpResponse(f'Пост номер {slug}')