from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseServerError, HttpResponseBadRequest, \
    HttpResponseForbidden
from django.shortcuts import render, redirect
from django.db import models

#Модуль для хранения представлений
# Create your views here.

menu = [{'title': 'Главное', 'url_name': 'home'},
        {'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Список студентов', 'url_name': 'students'}
        ]



data_bd = [{'id':5, 'FIO': 'Гришин Никита Сергеевич', 'interesting': 'Литература, Музыка, Фотография, Вязание, Программирование', 'is_sport': False},
            {'id':12, 'FIO': 'Ушаков Никита Юрьевич', 'interesting': 'Бокс, Плавание, Собирание марок, Туризм', 'is_sport': True},
            {'id':11, 'FIO': 'Солодкий Никита Олегович', 'interesting': 'Игры, Плетение бисером, Велосипед, Тренажёрный зал', 'is_sport': True},
           ]

def main(request):
    data = {'menu': menu,
            'posts': data_bd,
            }

    return render(request, 'women/index.html', context=data,)

def about(request):
    data={'menu': menu}

    #{% for p in menu %}
    #<a href="{% url '{{p.url_name}}' %}">{{p.title}}</a>
    #{% endfor %} ОНО НЕ РАБОТАЕТ ПОМОГИТЕЕЕЕ

    return render(request, 'women/about.html', context=data)

def one(request):
    raise serverError(exception=500)

def two(request):
    return HttpResponseForbidden('<h1>Данная страница давно заброшена... <br>'
                                 'Тут неуютно и пахнет сыростью..</h1>')

def three(request):
    return redirect('student/1/', permanent=True)

def four(request):
    return redirect('/year/2000/', permanent=True)

def student(request, student_id):
    if student_id > 13 or student_id < 1:
        return HttpResponseBadRequest('<h1>Ваш запрос сервер почему-то не смог прожевать<br>'
                                  'Попробуйте ещё раз :(</h1>')
    else:
        return HttpResponse(f' <h1> Студент № {student_id}</h1><br>'
                            f'<h2>{students[student_id]}</h2><br>'
                            f'<h2>{geburgstag[student_id]}</h2>')

def slug(request, slug1):
    return HttpResponse('<h1>Взгляни в адресную строку после "/"</h1>'
                        '<h2>Это метод Slug :3</h2>'
                        f'<h1>{slug1}</h1>')

def years(request, year_id):
    if year_id == 2023:
        return redirect('/year/2007/')
    elif year_id > 2014 or year_id < 2000:
        return HttpResponseBadRequest('<h1>Ваш запрос сервер почему-то не смог прожевать<br>'
                                      'Попробуйте ещё раз :(</h1>')
    else:
        return HttpResponse(f'<img src="{year[year_id]}" alt="{year_id}">')

def category(request,cat_id):
    return HttpResponse(f'<h1>{cat_id}</h1><br>'
                        f'<h2>Очень хорошая буковка, красивая :)</h2>')

def post_detail(request):
    res = request.GET
    t = dict(res)
    a=''
    for key,value in t.items():
        a+=f'{key}={value[0]}|'
    return HttpResponse(f'<h1>Добро-пожаловать на сервер "{a}"</h1>')
##################################################################################################################


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена :(<br></h1>'
                                '<a href="http://127.0.0.1:8000/">Пойдём лучше сюда:3</a>')

def serverError(exception):
    return HttpResponseServerError('<h1>Сервер немного тупит, ошибка 500 :(</h1>')

def badRequest(request, exception):
    return HttpResponseBadRequest('<h1>Ваш запрос сервер почему-то не смог прожевать<br>'
                                  'Попробуйте ещё раз :(</h1>')

def forbidden(request, exception):
    return HttpResponseForbidden('<h1>Данная страница давно заброшена... <br>'
                                 'Тут неуютно и пахнет сыростью..</h1>')

##################################################################################################################

students = {
    1:"Андронов Назар",
    2:"Андрюхин Даниил",
    3:"Асадов Наил",
    4:"Виноградский Иван",
    5:"Гришин Никита",
    6:"Ковалев Егор",
    7:"Короткая София",
    8:"Маганков Кирилл",
    9:"Палий Константин",
    10:"Покровский Данила",
    11:"Солодкий Никита",
    12:"Ушаков Никита",
    13:"Куленок Станислав"
}

geburgstag = {
    1: '09.05.2004',
    2: 'Мы не знаем, живой ли он вообще',
    3: '30.11.2004',
    4: '31.04.2004',
    5: '09.01.2004',
    6: '02.09.2004',
    7: '21.03.988',
    8: '14.06.2004',
    9: '05.12.2004',
    10: '02.02.2004',
    11: '04.07.2004',
    12: '15.08.2001',
    13: '32.13.2024'
}

year = {
    2000: 'https://i.pinimg.com/originals/fa/f4/66/faf466336c77e2765619197a5785887b.jpg',
    2001: 'https://inslav.ru/sites/default/files/styles/1920x1080/oldinslav/stories/pdf/2001_Russko-slav_kalendar.jpg?itok=N8yP7VvB',
    2002: 'https://tengrinews.kz/userdata/article/2021/article_1674/thumb_m/photo_2360.png',
    2003: 'https://calculator888.ru/img/skolko-dney/skolko-dney-v-2003-godu.jpg',
    2004: 'https://i.discogs.com/Ik4b7jXQOL3FywPf6MO55gCD9hhnwSbySsTQgWlreto/rs:fit/g:sm/q:90/h:600/w:423/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTcyNTY2/NjEtMTQzNzMzNTA3/OC05OTY3LmpwZWc.jpeg',
    2005: 'https://icdn.lenta.ru/images/0000/0097/000000972133/pic_1358529328.jpg',
    2006: 'https://calculat.io/ru/date/how-old-am-i-if-i-was-born-in/year--2006/generated.jpg',
    2007: 'https://cdn.fishki.net/upload/post/2021/02/19/3619213/1_120dfbbaf4926443d0ddfe0bc72c1e04.jpg',
    2008: 'https://www.chinahottour.ru/uploads/allimg/culture/shiershengxiao/2008%20year%20mouse1.jpg',
    2009: 'https://moneta-russia.ru/upload/monety-20-vek/10-rubl-2009-b.jpg',
    2010: 'https://znaki-zodiaka-goroskop.ru/wp-content/uploads/2010.jpg',
    2011: 'https://nauca.com.ua/wp-content/uploads/2011/12/2011.jpg',
    2012: 'https://upload.wikimedia.org/wikipedia/ru/d/dd/2012_Poster.jpg',
    2013: 'https://informatio.ru/upload/iblock/48c/140130mogoijil.jpg',
    2014: 'https://icdn.lenta.ru/images/2014/12/24/17/20141224170914709/pic_f239271ce9cff39efe3b7bc01ad7168a.jpg'
}
