from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from order.models import Product
from .forms import ProductForm, UserForm
from django import forms

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
        form_item = { ('product_%d' % product.id): forms.IntegerField(label=False,required=False) }

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

        # 小計金額に加算
        subtotal += int(product.price) * int(product_cnt)
        cart_data.append({'product_cnt': product_cnt, 'id': product.id ,'name': product.name})

    total_tax = int(round((subtotal * 0.1))) # 消費税
    subtotal_in_tax = int(subtotal) + int(total_tax) # 消費税込み金額

    # 送料
    if subtotal_in_tax < 5000:
        ship_cost = 800

    # 総合計金額
    total_price = int(subtotal_in_tax) + int(ship_cost)

    # 金額情報をセッションに追加
    request.session['subtotal'] = subtotal
    request.session['total_tax'] = total_tax
    request.session['ship_cost'] = ship_cost
    request.session['total_price'] = total_price

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
    return HttpResponse('購入 > 顧客情報・購入情報確認')

def order_thanks(request):
    """購入 > 完了"""
    return HttpResponse('購入 > 完了')
