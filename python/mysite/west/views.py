#coding=utf8
from django.core.context_processors import csrf
from django.shortcuts import render
from django.http import HttpResponse
from west.models import Character
# Create your views here.

def first_page(request):
	return HttpResponse("<p>西餐驾到<p>")


def staff(request):
	staff_list = Character.objects.all()
	staff_str = map(str,staff_list)
	context = {'label':' '.join(staff_str)}
	return render(request,'templay.html',context)
	#return HttpResponse("<p>" + ' '.join(staff_str) + "<p>")

def sec_page(request):
	return HttpResponse("<第二页面测试:>")


def templay(request):
	context = {}
	context['label'] = "Hello World"
	return render(request,'templay.html',context)

def staff_sec(request):
	staff_sec_list = Character.objects.all()
	return render(request,'staff_sec.html',{'staffs':staff_sec_list})

def form(request):
	return render(request,'form.html')

def rkt(request):
	rlt = request.GET['staff']
	return HttpResponse(rlt)

def post_form(request):
	ctx={}
	ctx.update(csrf(request))
	if request.POST:
		ctx['rlt']=request.POST['staff']
	return render(request,'post_form.html',ctx)
