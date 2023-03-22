from django.shortcuts import render

# Create your views here.
def virat(request):
    d={'name':'basha','age':'20'}
    return render(request,'virat.html',context=d)
