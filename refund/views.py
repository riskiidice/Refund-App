# -*- coding: utf-8 -*-
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect


from .forms import RefundForm
from .models import Refund
# from .services import THSMS
# Create your views here.
def refund_create(request):
    print request.POST
    form = RefundForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "การลงทะเบียนข้อมูลเสร็จสิ้น")
        # send_sms = THSMS(base_url="http://www.thsms.com")
        # method=send&username=riskiidice&password=e09be2&from=ETCTUTOR&to=$TO&message=$MESSAGE
        # response = send_sms.send_params(method="send",username="riskiidice",password="e09be2",from="ETCTUTOR",to=instance.mobile,message="สถาบันกวดวิชา ETC ได้รับข้อมูลการสมัครจากท่านแล้วกรุณารอการตอบกลับภายใน 1 วัน").execute()
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        if request.POST:
            messages.error(request,"การกรองข้อมูลไม่ครบถ้วน")
    context = {
     'title' : 'กรอกรายละเอียด',
     'form' : form
    }
    return render(request,'refund/form.html', context)

def refund_detail(request, id):
    instance = get_object_or_404(Refund,id=id)
    context = {
      "title": "รายละเอียด",
      "instance" : instance
    }
    return render(request,'refund/detail.html', context)
