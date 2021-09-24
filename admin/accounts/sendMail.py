from django.core.mail import send_mail
from django.template.loader import render_to_string
from elloadmin import settings

context = {
    "TWITTER_URL": "https://twitter.com/EllocentL",
    "FB_URL": "https://www.facebook.com/Ellocent-Labs-108118527408964",
    "INSTA_URL": "https://www.instagram.com/ellocentlabs/",
    "TELEGRAM_URL": "",
    "PRIVACY_URL": "https://ellocentlabs.com/privacy-policy",
    "TERMS_CONDITION": "https://ellocentlabs.com/terms-conditions",
    "http": "http",
    "Fb_IMG": "",
    "INSTA_IMG": "",
    "TWITTER_IMG": "",
    "LOGO_IMG": "https://pronto-core-cdn.prontomarketing.com/2/wp-content/uploads/sites/2675/2018/05/logo_sbs_r3-1.png"
}


def forgot_pass_mail(email, url,name):
    context["url"] = url
    context["name"] = name
    subject = "Reset password Mail"
    html_content = render_to_string('email/forgot_pass_mail.html', context)
    message = 'You are viewing this mail because you have requested to reset your password'
    try:
        send_mail(subject, message, settings.EMAIL_HOST_USER,
                [email], html_message=html_content)
    except Exception as e:
        print(str(e))

def signup(email, name):
    context["name"] = name
    subject = "Account Created"
    html_content = render_to_string('email/signup.html', context)
    message = 'Welcome to Ellocent Labs'
    try:
        send_mail(subject, message, settings.EMAIL_HOST_USER,
                [email], html_message=html_content)
    except Exception as e:
        print(str(e))
    
def verify_mail(email, url, name):
    context["url"] = url
    context["name"] = name
    subject = "Email Address Verification"
    html_content = render_to_string('email/email_verification.html', context)
    message = 'Please Confirm your email address'
    try:
        send_mail(subject, message, settings.EMAIL_HOST_USER,
                [email], html_message=html_content)
    except Exception as e:
        print(str(e))