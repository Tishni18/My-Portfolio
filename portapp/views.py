from django.shortcuts import render
from django.core.mail import send_mail,EmailMessage
from django.conf import settings
from django.shortcuts import redirect

def linkedin(request):
    linkedin_url = "https://www.linkedin.com/in/tishnirakesh"
    return redirect(linkedin_url)

def github(request):
    github_url = "https://github.com/Tishni18"
    return redirect(github_url)

def naukri(request):
    naukri_url = "https://www.naukri.com/mnjuser/profile"
    return redirect(naukri_url)

def home(request):
	return render(request,'index.html')

def profile(request):
	return render(request,'profile.html')
def projects(request):
	return render(request,'projects.html')






def contact(request):
    if request.method == 'POST':
        name_field = request.POST['name']
        email_field = request.POST['email']
        phone_field = request.POST['phone']
        message_field = request.POST['message']

        # Constructing the email message
        email_message = f"Name: {name_field}\nEmail: {email_field}\nPhone: {phone_field}\n\nMessage: {message_field}"

        # Sending Email
        send_mail(
            'Contact Form Submitted',
            email_message,
            email_field,  # Sender's email address
            ['myportfoilo2618@gmail.com'],  # Recipient's email addresses
        )

        return render(request, 'contact.html', {'name_field': name_field})

    else:
        return render(request, 'contact.html')
# def contact(request):
#     if request.method == 'POST':
#         name_field = request.POST['name']
#         email_field = request.POST['email']
#         phone_field = request.POST['phone']
#         message_field = request.POST['message']
#         #!...sending Email...!
#         send_mail(
#             'Contact Form Submitted From {}'.format(name_field),
#             message_field,
#             phone_field,
#             ['myportfoilo2618@gmail.com', email_field],
#             )
#         return render(request, 'contact.html', {'name_field': name_field})

#     else:
#         return render(request, 'contact.html')
# def contact(request):
#     if request.method == 'POST':
#         # Use get() method to retrieve values from POST dictionary
#         name_field = request.POST.get('name', '')
#         email_field = request.POST.get('email', '')
#         phone_field = request.POST.get('phone', '')
#         message_field = request.POST.get('message', '')
#         return render(request, 'contact.html', {'name_field': name_field})
#     else:
#         return render(request, 'contact.html')

# def contact(request):
#     if request.method == 'POST':
#         name_field = request.POST['name']
#         email_field = request.POST['email']
#         phone_field = request.POST['phone']
#         message_field = request.POST['message']
        
#         # Create an EmailMessage object
#         email = EmailMessage(
#             'Contact Form Submitted From {}'.format(name_field),
#             message_field,
#             settings.DEFAULT_FROM_EMAIL,
#             [settings.DEFAULT_FROM_EMAIL],
#             reply_to=[email_field],
#         )
        
#         # Send the email
#         email.send()

#         return render(request, 'contact.html', {'name_field': name_field})
#     else:
#         return render(request, 'contact.html')
