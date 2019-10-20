from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from django.views import View
from .models import*
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.core.mail import EmailMultiAlternatives
from django.views.decorators.cache import never_cache
from django.views.decorators.cache import cache_control
import string
from django.contrib import admin
from django.urls import path

# Create your views here.
from django.http import HttpResponse
import cloudinary
import cloudinary.api
import cloudinary.uploader


def index(request):
    fname = request.POST.get("fname")
    name = request.POST.get("name")
    feed = request.POST.get("feed")
    myfile=request.FILES.get("myfile")
    if fname is not None:
        if Signup.objects.filter(Firstname=fname).exists():
            a = Signup.objects.get(Firstname=fname)
            fname="%s"%(a.Firstname)
            pname=a.profile
            img1=a.img1
            img2=a.img2
            img3=a.img3
            img4=a.img4
            img5=a.img5
            img6=a.img6
            nick1="%s"%(a.nn1)
            nick2="%s"%(a.nn2)
            nick3="%s"%(a.nn3)
            nick4="%s"%(a.nn4)
            nick5="%s"%(a.nn5)
            print(nick2)
            print(img1)
            finn=[nick1,nick2,nick3,nick4,nick5]
            list2=[]
            for i in finn:
                if i is not None:
                    if i!="" and i!=" ":
                        list2.append(i)

            fiim=[img1,img2,img3,img4,img5,img6]
            list3=[]
            for i in fiim:
                if i is not None:
                    if i!="" and i!=" ":
                        list3.append(i)


            data={"pname":pname,"img1":img1,"img2":img2,"img3":img3,"img4":img4,"img5":img5,"img6":img6,"nick1":nick1,"nick2":nick2,"nick3":nick3,"nick4":nick4,"nick5":nick5,"fname":fname,"listm":list2,"listim":list3}
            return render(request, 'log.html',data)
    elif name is not None:
        # print(name, loc, email, phone, msg)
        # body = str(name) + "<br>" + str(loc) + "<br>" + str(email) + "<br>" + str(phone) + "<br>" + str(msg)
        # print(body)
        # send_mail("query",body, "%s <%s>"%(name,email), ["orendrasingh@gmail.com"])
        loc="Delhi"
        phone="7503408348"
        email="ogggy@gmail.com"
        msg=feed
        subject, from_email, to = 'Query', 'query@nbps.com', 'orendrasingh@gmail.com'
        text_content = 'This is an important message.'
        html_content = '<p>This is an <strong>important</strong> message.<br> Name : %s <br> Location : %s <br>  Phone : %s <br>  Email : %s <br>  Message : %s <br> </p>'%(name,loc,phone,email,msg)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        c = cloudinary.uploader.upload(request.FILES['myfile'])
        print(c)
        pf = c["url"]

        success = "Your query submitted successfully we will respond you soon... Thanks for visiting us."
        data = {"success": success,"im":pf}
        return render(request, "index.html", data)
    elif myfile is not None:
        c=cloudinary.uploader.upload(request.FILES['myfile'])
        # print(c)
        pf=c["url"]
        data={"im":pf}
        return render(request,"findex.html",data)

    return render(request,'index.html')

def signup(request):
    return render(request,"signup.html")

def log(request):
    return render(request,"log.html")