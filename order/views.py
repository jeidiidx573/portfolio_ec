from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from order.models import Product, Order, OrderItem
from .forms import ProductForm, UserForm
from django import forms

import random

# Create your views here.
def order_list(request):
    """購入 > 商品一覧"""
    # return HttpResponse('購入 > 商品一覧')
    product_list = Product.objects.all().filter(public=1).order_by('id')
    lists = []



    # 商品個数選択フォーム
    for product in product_list :
        items = {}

        # 商品ごとのinput要素生成
        form_item = {
            ('product_%d' % product.id): forms.IntegerField(initial=0,label=False,required=False,widget=forms.NumberInput(attrs={'class': 'form-control quantity-input'})) }

        product.price = "{:,}".format(product.price)
        items["product"] = product
        items["product_cnt_form"] = type('DynamicProductForm', (ProductForm,), form_item )

        lists.append(items)

    print(lists)

    context = {
        'product_list': product_list,
        'lists': lists,
        }
    return render(request, 'order/order_list.html', context)

def order_form(request):
    """購入 > 顧客情報入力"""
    # https://narito.ninja/blog/detail/46/

    # 金額初期値
    subtotal = 0
    total_tax = 0
    subtotal_in_tax = 0
    ship_cost = 0
    total_price = 0

    if request.method == 'POST':
        request.session['cart_data'] = request.POST
    else:
        return redirect('order:order_list')

    # セッション情報取得
    session_form_data = request.session.get('cart_data')

    if session_form_data is None:
        # セッション切れや、セッションが空でURL直接入力したら入力画面にリダイレクト。
        return redirect('order:order_list')

    # ------------------------
    form = UserForm()

    # POSTから購入商品情報をリスト化
    cart_data = []
    product_list = Product.objects.all().filter(public=1).order_by('id')
    for product in product_list :
        product_cnt = session_form_data[('product_%d' % product.id)] # 購入数

        if int(product_cnt) > 0:
            # 小計金額に加算
            product_total = int(product.price) * int(product_cnt)
            subtotal += product_total
            cart_data.append({'product_cnt': product_cnt, 'id': product.id ,'name': product.name, 'product_total': "{:,}".format(product_total), 'image':product.image })


    total_tax = int(round((subtotal * 0.1))) # 消費税
    subtotal_in_tax = int(subtotal) + int(total_tax) # 消費税込み金額

    # 送料
    if subtotal_in_tax < 5000:
        ship_cost = 800

    # 総合計金額
    total_price = int(subtotal_in_tax) + int(ship_cost)

    context = {
        'form': form,
        'session_form': session_form_data,
        'cart_data': cart_data,
        'subtotal': "{:,}".format(subtotal),
        'total_tax': "{:,}".format(total_tax),
        'ship_cost': "{:,}".format(ship_cost),
        'total_price': "{:,}".format(total_price),
        }
    return render(request, 'order/order_form.html', context)

def order_conf(request):
    """購入 > 顧客情報・購入情報確認"""

    if request.method == 'POST':
        form = UserForm(request.POST)
        request.session['user_data'] = request.POST
    else:
        return redirect('order:order_list')

    # セッション情報取得
    session_form_cart_data = request.session.get('cart_data')
    session_form_user_data = request.session.get('user_data')

    if session_form_cart_data is None:
        # セッション切れや、セッションが空でURL直接入力したら入力画面にリダイレクト。
        return redirect('order:order_list')

    print(session_form_cart_data)
    print(session_form_user_data)
    print(form)

    # 金額初期値
    subtotal = 0
    total_tax = 0
    subtotal_in_tax = 0
    ship_cost = 0
    total_price = 0

    # POSTから購入商品情報をリスト化
    cart_data = []
    product_list = Product.objects.all().filter(public=1).order_by('id')
    for product in product_list :
        product_cnt = session_form_cart_data[('product_%d' % product.id)] # 購入数

        if int(product_cnt) > 0:
            # 小計金額に加算
            product_total = int(product.price) * int(product_cnt)
            subtotal += product_total
            cart_data.append({'product_cnt': product_cnt, 'id': product.id ,'name': product.name, 'product_total': "{:,}".format(product_total), 'image':product.image })


    total_tax = int(round((subtotal * 0.1))) # 消費税
    subtotal_in_tax = int(subtotal) + int(total_tax) # 消費税込み金額

    # 送料
    if subtotal_in_tax < 5000:
        ship_cost = 800

    # 総合計金額
    total_price = int(subtotal_in_tax) + int(ship_cost)

    context = {
        'form': 'form',
        'session_form_cart_data': session_form_cart_data,
        'session_form_user_data': session_form_user_data,
        'cart_data': cart_data,
        'subtotal': "{:,}".format(subtotal),
        'total_tax': "{:,}".format(total_tax),
        'ship_cost': "{:,}".format(ship_cost),
        'total_price': "{:,}".format(total_price),
        }
    return render(request, 'order/order_conf.html', context)

def order_thanks(request):
    """購入 > 完了"""

    if request.method != 'POST':
        return redirect('order:order_list')

    # セッション情報取得
    session_form_cart_data = request.session.get('cart_data')
    session_form_user_data = request.session.get('user_data')

    if session_form_cart_data is None:
        # セッション切れや、セッションが空でURL直接入力したら入力画面にリダイレクト。
        return redirect('order:order_list')

    # 金額初期値
    subtotal = 0
    total_tax = 0
    subtotal_in_tax = 0
    ship_cost = 0
    total_price = 0

    # POSTから購入商品情報をリスト化
    cart_data = []
    product_list = Product.objects.all().filter(public=1).order_by('id')
    for product in product_list :
        product_cnt = session_form_cart_data[('product_%d' % product.id)] # 購入数

        if int(product_cnt) > 0:
            # 小計金額に加算
            product_total = int(product.price) * int(product_cnt)
            subtotal += product_total
            cart_data.append({'product_cnt': product_cnt, 'id': product.id ,'name': product.name, 'product_total': "{:,}".format(product_total), 'product_total_val': product_total, 'image':product.image })


    total_tax = int(round((subtotal * 0.1))) # 消費税
    subtotal_in_tax = int(subtotal) + int(total_tax) # 消費税込み金額

    # 送料
    if subtotal_in_tax < 5000:
        ship_cost = 800

    # 総合計金額
    total_price = int(subtotal_in_tax) + int(ship_cost)

    order_code = random.randrange(10000000,99999999)

    # DB登録order
    order = Order(
        status = 1,
        order_code = order_code,
        name = session_form_user_data['name'],
        kana = session_form_user_data['kana'],
        tel = session_form_user_data['tel'],
        mail = session_form_user_data['mail'],
        zip = session_form_user_data['zip'],
        address_1 = session_form_user_data['address_1'],
        subtotal = subtotal,
        total_tax = total_tax,
        ship_cost = ship_cost,
        total_price = total_price,
    )
    Order.save(order)

    # DB登録orderitem
    for data in cart_data:
        print(data['id'])
        product = Product.objects.filter(id=data['id'])[0]

        orderitem = OrderItem(
            order = order,
            product = product,
            name = product.name,
            price = product.price,
            count = data['product_cnt'],
            subtotal = data['product_total_val'],
        )

        OrderItem.save(orderitem)

    context = {
        'order_code': order_code,
        }
    return render(request, 'order/order_thanks.html', context)
