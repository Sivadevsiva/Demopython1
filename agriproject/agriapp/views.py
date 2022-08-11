from django.http import HttpResponse
from django.shortcuts import render, redirect

from .form import Agriform
from . models import Agri

# Create your views here.
def index(request):
    agri=Agri.objects.all()
    context={
        'agri_list':agri
    }
    return render(request,'index.html',context)
def detail(request,agri_id):
    ag=Agri.objects.get(id=agri_id)
    return render(request,"detail.html",{'agr':ag})
def add_agri(request):
    if request.method=='POST':
        name=request.POST.get('name')
        use = request.POST.get('use')
        About = request.POST.get('About')
        img = request.FILES['img']
        agri=Agri(name=name,use=use,About=About,img=img)
        agri.save()
    return render(request,"add.html")
def update(request,id):
    agri=Agri.objects.get(id=id)
    form=Agriform(request.POST or None,request.FILES,instance=agri)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'agri':agri})
def delete(request,id):
    if request.method=='POST':
        agri=Agri.objects.get(id=id)
        agri.delete()
        return redirect('/')
    return render(request,'delete.html')

