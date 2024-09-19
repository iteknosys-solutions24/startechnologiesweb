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

        subject_to_user = 'Star Technologies - Thank You for Your Query!'
        message_to_user = f"""
    <p>Dear {name},</p>
    <p>Thank you for reaching out to us. We appreciate your interest in our company and are happy to help answer any questions you may have. We will respond to your inquiry as soon as possible.</p>
    <p>You can check out the below link to view our Company Profile:</p>
    
        <b><i><a href="https://tinyurl.com/5cr8229h" target="_blank" style="font-size: large;">Our Company Profile</a></i></b>
    
    
    <p><b>Best Regards</b>,<br><i>Star Technologies</i></p>
    """
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]  # Replace with actual recipient email

            # Send thank you email to user
        send_mail(
                 subject_to_user,
                message_to_user,
                from_email,
                recipient_list,
                fail_silently=False,
                html_message=message_to_user  # Use HTML message
            )
        
        send_mail(
                'Client Enquiry Form: ',
                f'From: {name}\nEmail: {email}\n\nMessage:\n{message}',
            settings.EMAIL_HOST_USER,  # Replace with owner's email
            [settings.EMAIL_HOST_USER],  # Replace with owner’s email
            fail_silently=False,
             
            )

        messages.success(request, "Thank you for your message! We will get back to you soon.")
    
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
