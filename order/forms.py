from django import forms
from order.models import Product


class ProductForm(forms.Form):
    """商品選択フォーム"""
    pass

class UserForm(forms.Form):
    # 名前
    name = forms.CharField(
        label='氏名',
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control item', 'style': 'width:250px;'}),
    )
    # フリガナ
    kana = forms.CharField(
        label='フリガナ',
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control item', 'style': 'width:250px;'}),
    )
    # 電話番号
    tel = forms.CharField(
        label='電話番号',
        max_length=20,
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control item', 'style': 'width:250px;'}),
    )
    # メールアドレス
    mail = forms.EmailField(
        label='メールアドレス',
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control item'}),
    )
    # 郵便番号
    zip = forms.CharField(
        label='郵便番号',
        max_length=20,
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control item', 'style': 'width:250px;'}),
    )
    # 住所
    address_1 = forms.CharField(
        label='住所',
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control item'}),
    )
