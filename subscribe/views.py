from django.shortcuts import render

# Create your views here.
from Library.settings import EMAIL_HOST_USER
from .forms import Subscribe
from django.core.mail import send_mail, EmailMessage

# Create your views here.
#DataFlair #Send Email
def subscribe_email(request):
    sub = Subscribe()
    if request.method == 'POST':
        sub = Subscribe(request.POST)
        subject1 = 'Welcome to DataFlair'
        message1 = 'Hope you are enjoying your Django Tutorials'
        recepient = request.POST["Email"].strip()
        final_recepient_lst = None
        if ";" in recepient:
            final_recepient_lst = recepient.split(";")
        else:
            final_recepient_lst = [recepient]
        if final_recepient_lst:
            # send_mail(subject=subject1,message=message1, from_email= EMAIL_HOST_USER, recipient_list=final_recepient_lst, fail_silently = False)
            Msg = EmailMessage(subject=subject1, body=message1, from_email=EMAIL_HOST_USER, to=final_recepient_lst)
            Msg.attach_file(r"C:\Users\windows\Desktop\updated resume.docx")
            Msg.send(fail_silently = False)        
        return render(request, 'success.html', {'recepient': recepient})
    return render(request, 'index.html', {'form':sub})