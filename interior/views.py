import email
from http.client import HTTPResponse
import random
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView

from .models import Course, Category
from django.conf import settings

import requests
import xml.etree.ElementTree as ET
import hashlib

from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.views.decorators.csrf import csrf_exempt
import telebot

bot = telebot.TeleBot(settings.TOKEN, threaded=False)


@csrf_exempt
def worker(request):
    if request.META['CONTENT_TYPE'] == 'application/json':
        json_data = request.body.decode('utf-8')
        update = telebot.types.Update.de_json(json_data)
        bot.process_new_updates([update])
        return HttpResponse("")
    else:
        raise PermissionDenied


def send_telegram(a):
    bot.send_message(settings.GROUP_ID, a, parse_mode='HTML')


def main(request):
    return render(request, 'index.html')




def payment(request):
    a = request.POST
    # pg_amount
    # pg_currency
    # pg_description
    # pg_merchant_id
    # pg_order_id
    # pg_param1
    # pg_salt
    # pg_success_url
    # pg_user_contact_email
    # pg_sig
    usermail = a['email']
    name = a['name']
    course = a['course']
    phone = a['phone']
    param1 = 'hi'
    salt = 'bye'
    success_url = 'http://localhost:8000/success_pay/'
    order_id = random.randint(9999, 9999999)
    description = f'{name} - {course} - {phone}'
    md5hash = hashlib.md5(f"init_payment.php;{a['price']};USD;{description};{settings.MERCHANT_ID};{order_id};{param1};{salt};{success_url};{usermail};{settings.PAY_SECRET}".encode('utf-8')).hexdigest()
    #создаем хеш из последовательности данных
    the_data = {"pg_amount": a['price'], "pg_currency": 'USD', 
    "pg_description": description, "pg_merchant_id": settings.MERCHANT_ID, "pg_order_id": order_id,
    "pg_param1": param1, "pg_salt": salt, "pg_success_url": success_url, "pg_user_contact_email": usermail, "pg_sig": md5hash}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post("https://api.paybox.money/init_payment.php", data=the_data, headers=headers)
    responseXml = ET.fromstring(response.content.decode('utf-8'))
    resulturl = responseXml.find('pg_redirect_url')
    # print(response.content.decode('utf-8'))
    # получаем ссылку от freedompay
    # перенаправляем пользователя на эту ссылку
    return redirect(resulturl.text)



def coursedetail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'detail.html', {'course': course})




def categories(request): # все категории вместе список
    all_cat = Category.objects.all()
    
    return render(request, 'allcat.html', {'categories': all_cat})


def detailcategory(request, pk): # категория подробно
    category = get_object_or_404(Category, pk=pk)
    courses = Course.objects.filter(category=category)
    return render(request, 'detailcat.html', {'category': category, 'courses': courses})






def courses(request):
    allcourses = Course.objects.all()
    return render(request, 'courses.html', {'courses': allcourses})












def success_pay(request): # страница удачного платежа 
    # удачный платеж
    id_order = request.GET['pg_order_id']
    print(id_order)
    faf = {
        'ordint': id_order
    }
    return render(request, 'success_pay.html', context=faf)













def about(request): # страница о нас на примере можно сделать остальные страницы
    return render(request, 'about.html')

