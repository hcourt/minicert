from django.shortcuts import render

from app.models.customer import Customer


def index(request):
    customer_list = Customer.objects.order_by('-name')[:5]
    context = {
        'customer_list': customer_list,
    }
    return render(request, 'index.html', context)


