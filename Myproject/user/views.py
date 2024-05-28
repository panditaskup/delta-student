from django.shortcuts import render
from.models import *
from django.http import HttpResponse

# Create your views here.
def index(request):
    nbdata=newbatches.objects.all().order_by('-id')
    sdata=slider.objects.all().order_by('-id')
    ddata=placement.objects.all()
    mydict={"sdata":sdata,"nbdata":nbdata,"ddata":ddata}
    return render(request, 'user/index.html',mydict)

def about(request):
    return render(request, template_name='user/about.html')

def contact(request):
    if request.method=="POST":
        a=request.POST.get('name')
        b=request.POST.get('email')
        c=request.POST.get('mobile')
        d=request.POST.get('msg')
        contactus(name=a,email=b,mobile=c,message=d).save()
        return HttpResponse("<script>alert('Thanks for contacting with us...');location.href='/user/contact/'</script>")

    return render(request, template_name='user/contact.html')

def signin(request):
    if request.method=="POST":
        email=request.POST.get('email')
        passwd=request.POST.get('passwd')
        x=signup.objects.filter(passwd=passwd,email=email).count()
        if x==1:
            request.session['user']=email
            y=signup.objects.filter(email=email,passwd=passwd)
            request.session['userpic']=str(y[0].profile)
            request.session['username']=str(y[0].name)
            request.session['batchid']=str(y[0].batchid)
            return HttpResponse("<script>location.href='/student/index/'</script>")
        else:
            return HttpResponse("<script>alert('Your username or password is incorrect..');location.href='/user/signin/'</script>")
    return render(request, template_name='user/login.html')

def mynewbatches(request):
    batchdata=newbatches.objects.all().order_by('-id')
    md={"bdata":batchdata}
    return render(request, 'user/newbatches.html',md)

def registration(request):
    bdata=studentbatch.objects.all()
    md={"bdata":bdata}
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        passwd=request.POST.get('passwd')
        college=request.POST.get('college')
        course=request.POST.get('course')
        picture=request.FILES['fu']
        pyear=request.POST.get('pyear')
        batch=request.POST.get('batch')
        print(batch)
        x = signup.objects.filter(email=email).count()
        if x == 0:
            signup(name=name, email=email, mobile=mobile, college=college, course=course, pyear=pyear, profile=picture,
                   passwd=passwd, status='Pending',batchid=batch).save()
            return HttpResponse(
                "<script>alert('You are registered Successfuly...');location.href='/user/signin/'</script>")
        else:
            return HttpResponse("<script>alert('You are already registered...');location.href='/user/signup/'</script>")

    return render(request,'user/registration.html',md)

def ourfacility(request):
    return render(request, template_name='user/ourfacility.html')

def succes(request):
    clg=request.GET.get('college')
    year=request.GET.get('year')
    padata="";
    if clg is not None and year is not None:
        pdata = placement.objects.filter(college=clg,session=year)
    else:
        pdata=placement.objects.all()

    collegedata = college.objects.all().order_by('-id')
    sdata = session_year.objects.all().order_by('-id')

    md = {"cdata": collegedata, "sdata": sdata, "pdata": pdata}
    return render(request, 'user/succes.html', md)



def feedback(request):
    if request.method=="POST":
        yourname=request.POST.get('yourname')
        image=request.FILES['fu']
        college=request.POST.get('college')
        message=request.POST.get('message')
        myfeedback(yourname=yourname,image=image,college=college,message=message).save()
        return HttpResponse(
            "<script>alert('Your feedback sent Successfuly...');location.href='/user/feedback/'</script>")
    return render(request, template_name='user/feedback.html')

def digital(request):
    return render(request, template_name='user/digital.html')




