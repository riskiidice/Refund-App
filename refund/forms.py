# -*- coding: utf-8 -*-
from django import forms

from .models import Refund

class RefundForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'ชื่อจริง'}))
    surname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'นามสกุลจริง'}))
    mobile = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'เบอร์มือถือ( รับ sms )'}))
    account = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'ธนาคาร เช่น ไทยพาณิชย์'}))
    account_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'ชื่อบัญชี เช่น นายกอไก่ ขอไข่'}))
    account_number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'เลขบัญชีธนาคาร'}))
    class Meta:
        model  = Refund
        fields = [
          "name",
          "surname",
          "mobile",
          "account",
          "account_name",
          "account_number"
        ]
