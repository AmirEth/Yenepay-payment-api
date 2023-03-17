from django.shortcuts import render
import requests
from .models import Product, Seller


def payment_with_cart(request):
    products = Product.objects.all()

    return render(request, 'index-cart.html', {'products': products})


def success(request):
    ii = request.GET.get('itemId')
    total = request.GET.get('TotalAmount')
    moi = request.GET.get('MerchantOrderId')
    ti = request.GET.get('TransactionId')
    status = request.GET.get('Status')
    url = 'https://testapi.yenepay.com/api/verify/pdt/'
    datax = {
        "requestType": "PDT",
        "pdtToken": "Q1woj27RY1EBsm",
        "transactionId": ti,
        "merchantOrderId": moi
    }
    x = requests.post(url, datax)
    if x.status_code == 200:
        print("It's Paid")
    else:
        print('Invalid payment process')
    return render(request, 'success.html', {'total': total, 'status': status, })


def cancel(request):
    return render(request, 'cancel.html')
