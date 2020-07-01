from django.shortcuts import render
from django.http import HttpResponse

from order.models import Product

# Create your views here.
def order_list(request):
    """購入 > 商品一覧"""
    # return HttpResponse('購入 > 商品一覧')
    product_list = Product.objects.all().order_by('id')
    return render(request,
        'order/order_list.html')

def order_form(request):
    """購入 > 顧客情報入力"""
    return HttpResponse('購入 > 顧客情報入力')

def order_conf(request):
    """購入 > 顧客情報・購入情報確認"""
    return HttpResponse('購入 > 顧客情報・購入情報確認')

def order_thanks(request):
    """購入 > 完了"""
    return HttpResponse('購入 > 完了')
