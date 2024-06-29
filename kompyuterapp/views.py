from django.shortcuts import render
from .models import Kompyuter
# Create your views here.



def Kompyuter_data(request):
    kompyuters= Kompyuter.objects.all()
    context={
        'kompyuters':kompyuters,
    }



    return render(request=request,template_name='kompyuter.html',context=context)


# def account(request)    