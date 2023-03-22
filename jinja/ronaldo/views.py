from django.shortcuts import render

# Create your views here.
def ronaldo(request):
    d={'name':'Ronaldo','age':'30','game':'football'}
    return render(request,'ronaldo.html',context=d)

def basha(request):
    d={'name':'Basha','age':'20','game':'football'}
    return render(request,)