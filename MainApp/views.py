from django.shortcuts import render, HttpResponse, Http404
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist

user = {
    "name": "Артём",
    "last_name": "Мовланов"
}


def home(request):
    context = {
        "user": user,
        "page_title": "Главная",
    }
    return render(request, 'index.html', context)


def about(request):
    html_text = "Имя: <b>Иван</b><br>Отчество: <b>Петрович</b><br>Фамилия: <b>Иванов</b><br>телефон: " \
                "<b>8-923-600-01-02</b><br>email: <b>vasya@mail.ru</b>"
    return HttpResponse(html_text)


def get_items(request, id):
    try:
        item = Item.objects.get(id=id)
        context = {
            "page_title": "Описание товара",
            "item": item
        }
        return render(request, 'item.html', context)
    except ObjectDoesNotExist:
        raise Http404


def get_items_list(request):
    context = {
        "items": Item.objects.all(),
        "page_title": "Список товаров",
    }
    return render(request, 'items_list.html', context)
