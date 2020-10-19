from django.shortcuts import render, redirect
from django.db import connection
from django.contrib import messages

def dictfetchall (cursor):
    columns = [col[0] for col in cursor.description]
    return[dict(zip(columns, row)) for row in cursor.fetchall()]


def index(request):
    with connection.cursor() as cursor:
        cursor.execute('SET SEARCH_PATH to rianabelio')
        cursor.execute('SELECT * FROM PRODUCT WHERE id_product in (SELECT count FROM position)')
        product_info = dictfetchall(cursor)[0] 
        cursor.execute('SELECT the_color FROM COLOUR WHERE id_product in (SELECT count FROM position)')
        color_info = dictfetchall(cursor)
        if (product_info['id_product'] == 10):
            cursor.execute('UPDATE POSITION SET count =  1')
        else:
            cursor.execute('UPDATE POSITION SET count = count + 1')
        
        print(product_info)
        print(color_info)
        return render(request, 'home.html', {'product_info':product_info, 'color_info':color_info})
    