from django.shortcuts import render
from django.core.mail import send_mail
from sendemail.settings import EMAIL_HOST_USER

# Create your views here.


def index(request):
    if request.method == 'POST':
        mail = request.POST['email']
        send_mail("Mail Test", "I'm Testing Django mail send",
                  EMAIL_HOST_USER, [mail])

    return render(request, "index.html")
