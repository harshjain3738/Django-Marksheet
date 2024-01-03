from django.shortcuts import render

def marksheet(request):
    if request.method=="POST":
        s1=eval(request.POST.get("sub1"))
        s2=eval(request.POST.get("sub2"))
        s3=eval(request.POST.get("sub3"))
        s4=eval(request.POST.get("sub4"))
        s5=eval(request.POST.get("sub5"))
        t=s1+s2+s3+s4+s5
        per=t*100/500
        if per>=75:
            div="first division"
        elif per>=55:
            div="second division"
        elif per>=33:
            div="third division"
        else:
            "fail !!!"
        data={
            'per':per,
            'total':t,
            'div':div
        } 
        return render(request,"index.html",data)               
    return render(request,"index.html")

# Create your views here.
