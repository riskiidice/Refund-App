# -*- coding: utf-8 -*-
from django import forms

from .models import Refund

class RefundForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'ชื่อจริง'}))
    surname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'นามสกุลจริง'}))
    student_id = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'หมายเลขลำดับ'}))
    mobile = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'เบอร์มือถือ( รับ sms )'}))
    account = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'ธนาคาร เช่น ไทยพาณิชย์'}))
    account_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'ชื่อบัญชี เช่น นายกอไก่ ขอไข่'}))
    account_number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'เลขบัญชีธนาคาร ไม่ต้องใส่ - หรือ ช่องว่าง'}))
    class Meta:
        model  = Refund
        fields = [
          "name",
          "surname",
          "student_id",
          "mobile",
          "account",
          "account_name",
          "account_number"
        ]
