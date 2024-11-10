# imports
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from .models import account, tempuser, temppwd

#email essantioal imports
from .messages import reset_password_success, reset_password_request, singin_request, msg
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def index(request):
    "index for website"
    return redirect('welcome')


def welcome(request):
    "welcome page rendering"
    return render(request, 'main/welcome.html')


def loginPage(request):
    "login page rendering"
    content = {'title': ' - Login', 'value': 0, 'usnme': '', 'pswrd': ''}
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        usr = authenticate(request, username=username, password=password)

        if usr is not None:
            login(request, usr)
            return redirect('home')

        elif usr is None:
            current_usr = account.objects.filter(username=username)
            content['usnme'] = username
            content['pswrd'] = password

            if not len(current_usr): content['value'] = 1

            else: content['value'] = 2

    return render(request, 'main/login.html', content)


def logoutPage(request):
    logout(request)
    return redirect('welcome')


def singIn(request):
    "rendering singin pages"
    context = {
        'title': ' - Sing in',
        'mode': 1,
        'val1': '',
        'val2': '',
        'val3': '',
        'val4': '',
        'val5': ''
    }

    if request.method == 'POST':

        if 'name' in request.POST.keys():
            phno = request.POST['mobile']
            v1 = request.POST['name']
            v2 = request.POST['dob']
            if account.objects.filter(mobile=phno):
                context['val1'] = v1
                context['val2'] = v2
                context['val3'] = phno
                return render(request, 'main/form-userinfo.html', context)
            js = tempuser(name=v1, mobile=phno, dob=v2)
            js.save()
            context['mode'] = 2
            context['val1'] = js.id
            return render(request, 'main/form-eup.html', context)

        if 'uname' in request.POST.keys():
            tmpusr = tempuser.objects.filter(id=request.POST['value2'])[0]
            uanme = request.POST['uname']
            email = request.POST['email']
            context['val1'] = tmpusr

            if account.objects.filter(
                    username=uanme) or account.objects.filter(email=email):
                context['mode'] = 2
                context['val2'] = uanme
                context['val3'] = email
                context['val4'] = request.POST['pas1']

                if account.objects.filter(username=uanme): context['val5'] = 1
                elif account.objects.filter(email=email): context['val5'] = 2

                return render(request, 'main/form-eup.html', context)

            tmpusr.username = uanme
            tmpusr.email = email
            tmpusr.password = request.POST['pas1']
            tmpusr.save()
            context['mode'] = 3
            send_mail(
                f"{ singin_request['subject'] }",  #Topic
                f"{ msg }{ singin_request['message1'] }{ tmpusr.code } { singin_request['message2'] } ",  #Message
                'settings.EMAIL_HOST_USER',  #Senader Eamil
                [tmpusr.email],  #Recever Email
                fail_silently=False)

            return render(request, 'main/form-varification.html', context)

    if 'varfc' in request.POST.keys():
        usercd = eval(request.POST['varfc'])
        io = tempuser.objects.filter(id=request.POST['sand'])[0]
        if usercd != io.code:
            context['mode'] = 3
            context['val1'] = io
            context['val2'] = usercd
            return render(request, 'main/form-varification.html', context)

        newusr = account(name=io.name,
                         mobile=io.mobile,
                         dob=io.dob,
                         username=io.username,
                         email=io.email,
                         is_active=True)
        newusr.set_password(io.password)
        newusr.save()
        io.delete()
        login(request, newusr)
        return redirect('home')

    return render(request, 'main/form-userinfo.html', context)


def renamePassword(request):
    "rendering rename password pages"
    context = {
        'title': ' - Reset Password',
        'mode': 1,
        'value': '',
        'inpt': '',
        'value2': ''
    }
    if request.method == 'POST':

        if 'varfc' in request.POST.keys():

            context['mode'] = 2
            usercode = eval(request.POST['varfc'])
            v2 = request.POST['value2']
            io = temppwd.objects.filter(id=v2)[0]
            if usercode != io.code:
                context['value'] = 1
                context['value2'] = io
                context['inpt'] = usercode
                return render(request, 'main/rename-varify.html', context)

            das = account.objects.filter(id=io.userId)[0]
            das.set_password(io.password)
            das.save()
            io.delete()
            send_mail(
                f"{ reset_password_success['subject'] } ",  #Topic
                f"{ msg }{reset_password_success['message1']}",  #Message
                'settings.EMAIL_HOST_USER',  #Sender Email
                [das.email],  #Recever Eamil
                fail_silently=False)

            return redirect('login')

        usrname = request.POST['uname']
        usr = account.objects.filter(username=usrname)
        if not (usr):
            context['value'] = usrname
            context['value2'] = request.POST['pas1']
            return render(request, 'main/rename-rename.html', context)

        se = temppwd(password=request.POST['pas1'],
                     userId=usr[0].id,
                     email=usr[0].email)
        se.save()
        context['value2'] = se

        send_mail(
            f"{ reset_password_request['subject'] }",  #Topic
            f"{ msg }{ reset_password_request['message1'] }{se.code} {reset_password_request['message2']}",  #Message
            'settings.EMAIL_HOST_USER',  #Senader Eamil
            [usr[0].email],  #Recever Email
            fail_silently=False)
        context['mode'] = 2
        return render(request, 'main/rename-varify.html', context)

    return render(request, 'main/rename-rename.html', context)
