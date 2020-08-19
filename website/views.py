from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return render(request,'home.html',{})


def contact(request):
    if request.method == 'POST':
        
        message_name = request.POST['message-name']
        message_email = request.POST['message-email'] 
        message = request.POST['message']

        send_mail(
           message_name ,#subject
           message,#message
           message_email,#from
           ['rado7711@yahoo.co.uk'] ,# to email
           fail_silently=False,
        )

        
        return render(request, 'contact.html',{
            'name':message_name, 'email':message_email, 'message':message,
        })
    else:
       #return this page do some ather staff 
        return render(request, 'contact.html',{})