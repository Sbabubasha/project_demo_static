from django.shortcuts import render

# Create your views here.
def ronaldo(request):
    d={'name':'ronaldo','age':'30','game':'football'}
    return render(request,'')