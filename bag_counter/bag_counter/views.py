from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# from .models import CountModel

def page2(request):
    
    return render(request,"sample page2.html")


def numberform(request):
    n= None
    tet= None
    try:
        if request.method=="POST":
            n=int(request.POST.get('number'))
            tet=request.POST.get('text')
            
            print(n)
            print(tet)
            
        
    except:
        pass
    return render(request,"log.html",{'output': n , 'text' : tet})

    # return render(request,"sample page1.html",{'output': n , 'text' : tet})

def count_view(request):
    count = CountModel.objects.first().count
    context = {'count': count}
    return render(request, 'count.html', context)