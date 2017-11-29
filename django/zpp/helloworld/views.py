from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from models import User


def hello(request):
    return render(request, 'hello.html', {"data": "Hello Zpp"})


def insert(request, name, birthday, gender):
    usr = User(name=name, birthday=birthday, gender=gender)
    usr.save()
    return HttpResponse(usr["id"])


def delete(request, uid, is_active):
    usr = User.objects.filter(id=uid, is_active=is_active)
    usr.delete()
    return HttpResponseRedirect('/hello/')


def query(request, uid):
    usr = User.objects.get(id=uid)
    return HttpResponse(usr["name"])


def update(request, name, birthday):
    usr = User.objects.get(name=name)
    usr["birthday"] = birthday
    usr.save()
    return HttpResponse("ok")


@csrf_protect
def add(request):
    if request.method == "GET":
        return render(request, "form.html", {"action": "/hello/add/"})
    else:
        u = User(name=request.POST["name"], birthday=request.POST["birthday"], gender=request.POST["gender"])
        u.save()
        return HttpResponseRedirect("/hello/")


def index(request):
    return render(request, 'list.html', {"users": User.objects.all()})


def edit(request):
    if request.method == "GET":
        u = User.objects.get(id=request.GET["id"])
        return render(request, "form.html", {"action": "/hello/edit/", "u": u.__dict__})
    else:
        u = User.objects.get(id=request.GET["id"])
        u.name = request.POST["name"]
        u.birthday = request.POST["birthday"]
        u.gender = request.POST["gender"]
        u.save()
        return HttpResponseRedirect("/hello/")




