from django.shortcuts import render
from .models import Account

def account_list(request):
    accounts=Account.objects.all().order_by('username')
    return render(request, 'accounts/accountList.html',{'accounts':accounts})
