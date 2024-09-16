from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.urls import reverse

# Create your views here.

def index_view(request):
    if request.method == 'POST':
        name = request.POST.get('cname')
        email = request.POST.get('cemail')
        phone = request.POST.get('cphone')
        subject = request.POST.get('csubject')
        message = request.POST.get('cmessage')

        send_mail(
                'Client Enquiry Form: ',
                f'From: {name}\n Email: {email}\n\n Message:\n{message}',
            settings.EMAIL_HOST_USER,  # Replace with owner's email
            [settings.EMAIL_HOST_USER],  # Replace with owner’s email
            fail_silently=False,
             
            )

            # Send thank you email to user
        send_mail(
                'Star Technologies',
                'Thank you for your message. We will get back to you shortly.',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )

        messages.success(request, "Thank you for your message! We will get back to you soon.")
        print('no sent')
        return redirect('index-view')

    return render(request, 'html/index_view.html')



def products_view(request):
    return render(request, 'html/prod_view.html')


def accept_cookies(request):
    response = redirect('index-view')  # Redirect to a relevant page
    response.set_cookie('cookie_consent', 'accepted', max_age=31536000)  # 1 year
    return response

def reject_cookies(request):
    response = redirect('index-view')  # Redirect to a relevant page
    response.set_cookie('cookie_consent', 'rejected', max_age=31536000)  # 1 year
    return response


def cookie_policy(request):
    return render(request, 'html/cookie_policy.html')