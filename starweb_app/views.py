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
    <p>Thank you for reaching out to us. We appreciate your interest in our company and we are happy, answer any questions you may have. We will respond to your inquiry as soon as possible.</p>
    <p>Click here to view <i><a href="https://tinyurl.com/5cr8229h" target="_blank" style="font-size: large;">Our Company Profile</a></i></p>
    
        
    
    
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
                f'Client Name: {name}\n\nClient Email: {email}\n\n Subject: {subject}\n\nClient Message:\t{message} ',
            settings.EMAIL_HOST_USER,  # Replace with owner's email
            [settings.EMAIL_HOST_USER],  # Replace with owner’s email
            fail_silently=False,
             
            )

        messages.success(request, "Thank you for your message! We will get back to you soon....!!")
    
        return redirect('index-view')

    return render(request, 'html/index_view.html')



def products_view(request):
    return render(request, 'html/prod_view.html')



#------------------------Copiers--------------------------------
def BP_20M_31_28_24_22_pdf_view(request):
    return render(request, 'html/prod_view.html')

def BP_20C_20_25_10C20_pdf_view(request):
    return render(request, 'html/prod_view.html')

def BP_30M_35_31_28_pdf_view(request):
    return render(request, 'html/prod_view.html')

def PC_311W_MC_320F_merged(request):
    return render(request, 'html/prod_view.html')

def MC_251FW(request):
    return render(request, 'html/prod_view.html')

def M_2040dn_2540dn_2640idw(request):
    return render(request, 'html/prod_view.html')

def BP_30C25Z_BP_30C25ZT(request):
    return render(request, 'html/prod_view.html')

def BP_50C26_50C31_50C36_50C45(request):
    return render(request, 'html/prod_view.html')

def M_8124cidn(request):
    return render(request, 'html/prod_view.html')

#-----------------Displays----------------------------

def PN_Q901_801_701_6011(request):
    return render(request, 'html/prod_view.html')

def PN_HW_751(request):
    return render(request, 'html/prod_view.html')

def PN_50TC1(request):
    return render(request, 'html/prod_view.html')

def Display_R65_2024_2(request):
    return render(request, 'html/prod_view.html')

def R_75_inch(request):
    return render(request, 'html/prod_view.html')

def display_r_series_86_inch(request):
    return render(request, 'html/prod_view.html')

#------------------------------------------------------------


#-----------------------Projectors-------------------------------------

def viewsonic_all_pdf(request):
    return render(request, 'html/prod_view.html')

def epson_all_pdf(request):
    return render(request, 'html/prod_view.html')

def panasonic_all_pdf(request):
    return render(request, 'html/prod_view.html')

def infocus_all_pdf(request):
    return render(request, 'html/prod_view.html')

def benq_all_pdf(request):
    return render(request, 'html/prod_view.html')

def optoma_all_pdf(request):
    return render(request, 'html/prod_view.html')

#------------------------------------------------------------

#-------------------Other Products---------------------------
def fujitsu_all_pdf(request):
    return render(request, 'html/prod_view.html')

def hp_all_pdf(request):
    return render(request, 'html/prod_view.html')

#------------------------------------------------------------
