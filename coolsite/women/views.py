from django.http import HttpResponse
from django.shortcuts import render

#Модуль для хранения представлений
# Create your views here.

def main(request):
    return HttpResponse('<h1>Добро-пожаловать на сервер "Шизофрения"</h1>')

def one(request):
    return HttpResponse('<h1> Это как-бы вторая страница </h1><br>'
                        '<h3>:)</h3>')

def two(request):
    return HttpResponse('<h1> Это как-бы третья страница </h1><br>'
                        '<h3>:)</h3>')

def student(request, student_id):
    if student_id > 13 or student_id < 1:
        return HttpResponse(f' <h1> Такой студент у нас не проживает :( </h1>')
    else:
        return HttpResponse(f' <h1> Студент № {student_id}</h1><br>'
                            f'<h2>{students[student_id]}</h2><br>'
                            f'<h2>{geburgstag[student_id]}</h2>')

def slug(request):
    return HttpResponse('<h1>Взгляни в адресную строку после "/"</h1>'
                        '<h2>Это метод Slug :3</h2')

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


