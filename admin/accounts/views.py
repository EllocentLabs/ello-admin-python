from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.hashers import check_password
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect, render
from django.utils.translation import ugettext as _

from admin.accounts.jwt import decode_data, encode_data
from admin.accounts.models import Admin
from admin.accounts.sendMail import forgot_pass_mail


def dashboard(request):
    title = "Dashboard"
    return render(request, 'dashboard.html', locals())

    
def login(request):
    try:
        if request.method == "POST":
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(email=email, password=password)
            if user:
                auth_login(request, user)
                messages.success(request, 'Welcome To Ellocent Labs.')
            else:
                messages.warning(request, 'Wrong credentials.')
        return redirect('/')
    except Exception as e:
        print(e)
        messages.error(request, 'An error occurred, please try again.')
        return redirect('/')


def logout_user(request):
    logout(request)
    return redirect('/')


def change_password(request):
    if request.method == "POST":
        if check_password(request.POST.get('oldPassword'), request.user.password):
            if request.POST.get('password') == request.POST.get('cPassword'):
                if 5 < len(request.POST.get('cPassword')) <= 15:
                    request.user.set_password(request.POST.get('cPassword'))
                    request.user.save()
                    messages.success(request, _(
                        'Password Successfully Changed.'))
                    return redirect("/")
                else:
                    messages.warning(request, _(
                        'Password can not be less than 6.'))
            else:
                messages.warning(request, _(
                    'Password and Confirm Password  Does Not Match.'))
        else:
            messages.warning(request, _('Wrong Old Password.'))
        return redirect(change_password)
    return render(request, "admin/change_password.html", {"title": "Change Password"})


def forgot_password(request):
    title = _('Forgot Password')
    if request.method == "POST":
        email = request.POST.get('email')
        user = Admin.objects.filter(email=email)
        if user.exists():
            user_obj = user.first()
            name = user_obj.name
            user_id = user_obj.id
            base_url = "http://" +str(get_current_site(request)) + "/login/create-new-password/"
            try:
                path = encode_data(str(user_id), str(base_url))

                forgot_pass_mail(email, path, name)

                messages.success(request, _('Password reset sent to your Email'))
                user = Admin.objects.get(id=user_id)
                user.forgotStatus = True
                user.save()
                return redirect('/')
            except:
                messages.error(request, _('Something went wrong'))
        else:
            messages.warning(request, _('Email not in database'))
    return render(request, 'forgot-password/forgot_password.html', locals())


def reset_password(request, token):
    uid = decode_data(token)
    if request.method == "POST":
        password = request.POST.get('password1')
        cpassword = request.POST.get('password2')
        user = Admin.objects.get(id=uid)
        if password == cpassword:
            user.set_password(cpassword)
            user.forgotStatus = False
            user.save()
            messages.success(request, _('Password has been Changed.'))
        else:
            messages.warning(request, _(
                'Password and confirm password did not matched.'))
        return redirect('/')
    else:
        user = Admin.objects.get(id=uid)
        url_exist = user.forgotStatus
        if(url_exist == False or uid == False):
            messages.warning(request, 'Link Expired')
            return redirect('/')
        return render(request, "forgot-password/reset_password.html", {"title": "Change password"})



