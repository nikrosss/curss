from django.shortcuts import render, Http404
import os

# Create your views here.

def home(request):

    site_name = 'NikRos(new stile)'

    #Заголовок страницы
    list_name = 'Главная страница'

    # приветствие
    privet = 'уважаемые гости'

    #вводный текст берем из файла (далее сделаем вывод из БД для всех подобных решений)
#    my_file = open('./static/text/hi_text.txt', 'r')
 #   privet_text = [a.strip() for a in my_file.readlines()]
    my_file = open('./static/text/hi_text.txt', 'r')
    t = my_file.read()


    return render(request, 'index.html', {'site_name':site_name, 'privet': privet,
                                          #'privet_text':privet_text[0],
                                          't': t,
                                          'list_name': list_name} )

def its_me(request, self):
    site_name = 'NikRos(new stile)'

    list_name = 'Обо мне...'

    return render (request, 'its_me.html', {'site_name':site_name,
                                            'list_name': list_name})


def jobs(request):
    site_name = 'NikRos(new stile)'

    list_name = 'Моя карьера'

    return render (request, 'my_jobs.html', {'site_name':site_name,
                                           'list_name': list_name})
