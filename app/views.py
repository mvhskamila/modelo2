from django.shortcuts import render,redirect
from app.models import *

# Create your views here.

#var global
td_global=''
#inicio
def entrar(request):
    frota='0202'
    adm='0101'
    Q='1'
    w='2'

    if 'user' in request.GET:
        Q = request.GET['user']   
    if 'pwd' in request.GET:
        w = request.GET['pwd']

    if Q == frota and  w==adm:
        url_show='home.html'
    else:
        url_show='entrar.html'


    return render(request,url_show)

def home(request):
    return render(request,'home.html')

def inicio(request):
    return render(request,'ini.html')

def index(request):
    mem=tab_td.objects.all()
    return render(request,'index.html',{'mem':mem})

def add(request):
    return render(request,'add.html')

def addrec(request):
   
    
    td_data=request.POST['data']
    td_placa=request.POST['placa']
    td_motorista=request.POST['motorista']
    td_ajudante=request.POST['ajudante']

    td_td=request.POST['td']
    td_km=request.POST['km']
    td_cliente=request.POST['cliente']
    td_nota_1=request.POST['nota_1']
    td_nota_2=request.POST['nota_2']

    td_p2=request.POST['p2']
    td_p5=request.POST['p5']
    td_p8=request.POST['p8']
    td_p13=request.POST['p13']
    td_p20=request.POST['p20']
    td_p45=request.POST['p45']
    
    td_saida=request.POST['saida']
    td_entrada=request.POST['entrada']
    td_OBS=request.POST['OBS']
    
    
    
    mem=tab_td(td=td_td,
               data=td_data,
               placa=td_placa,
               motorista=td_motorista,
               ajudante=td_ajudante,
               km=td_km,
               cliente=td_cliente,
               nota_1=td_nota_1,
               nota_2=td_nota_2,
               p2=td_p2,
               p5=td_p5,
               p8=td_p8,
               p13=td_p13,
               p20=td_p20,
               p45=td_p45,
               saida=td_saida,
               entrada=td_entrada,
               OBS=td_OBS
              
               ) 
                         
    mem.save()
    return redirect("/index")

def delete(request,id):
    mem=tab_td.objects.get(id=id)
    mem.delete()
    return redirect("/index")

def update(request,id):
    print('1')
    mem=tab_td.objects.get(id=id)
    return render(request,'update.html',{'mem':mem})

def uprec(request,id):

    td_data=request.POST['data']
    td_placa=request.POST['placa']
    td_motorista=request.POST['motorista']
    td_ajudante=request.POST['ajudante']

    td_td=request.POST['td']
    td_km=request.POST['km']
    td_cliente=request.POST['cliente']
    td_nota_1=request.POST['nota_1']
    td_nota_2=request.POST['nota_2']

    td_p2=request.POST['p2']
    td_p5=request.POST['p5']
    td_p8=request.POST['p8']
    td_p13=request.POST['p13']
    td_p20=request.POST['p20']
    td_p45=request.POST['p45']
    
    td_saida=request.POST['saida']
    td_entrada=request.POST['entrada']
    td_OBS=request.POST['OBS']
    
    mem=tab_td.objects.get(id=id)
    mem.td=td_td
    mem.data=td_data
    mem.placa=td_placa
    mem.motorista=td_motorista
    mem.ajudante=td_ajudante
    mem.km=td_km
    mem.cliente=td_cliente
    mem.nota_1=td_nota_1
    mem.nota_2=td_nota_2
    mem.p2=td_p2
    mem.p5=td_p5
    mem.p8=td_p8
    mem.p13=td_p13
    mem.p20=td_p20
    mem.p45=td_p45
    mem.saida=td_saida
    mem.entrada=td_entrada
    mem.OBS=td_OBS
    
    mem.save()
   
    return redirect("/index")

#------------------------------------------------------------

def pesq(request):
    if 'q' in request.GET:
        q = request.GET['q']
        mem  = tab_td.objects.filter(td__icontains=q)
        #multiple_q = Q(Q(cliente__icontains=q) | Q(data__icontains=q))
        mem  = tab_td.objects.filter(td=q)
        print(mem )
    else:
        mem  =tab_td.objects.all()

    context = {
        'mem' :mem 
    }
    return render(request, 'pes.html',context)
