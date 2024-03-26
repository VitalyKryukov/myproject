from django.shortcuts import render
from django.db.models import Sum
from myapp5.models import Product


def total_in_db(request):
    """
    Вариант1: Считаем сумму в БД
    :param request:
    :return:
    """
    total = Product.objects.aggregate(Sum('quantity'))
    context = {
        'title': 'Общее количество посчитано в базе данных',
        'total': total,
    }
    return render(request, 'myapp6/total_count.html', context)


def total_in_view(request):
    """
    Вариант 2: Считаем сумму в представлении
    :param request:
    :return:
    """
    products = Product.objects.all()
    total = sum(product.quantity for product in products)
    context = {
        'title': 'Общее количество посчитано в представлении',
        'total': total,
    }
    return render(request, 'myapp6/total_count.html', context)


def total_in_template(request):
    """
    Вариант 3: Сумма посчитанная в модели, через вызов в шаблоне
    :param request:
    :return:
    """
    context = {
        'title': 'Общее количество посчитано в шаблоне',
        'products': Product,
    }
    return render(request, 'myapp6/total_count.html', context)
