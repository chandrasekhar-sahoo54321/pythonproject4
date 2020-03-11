from django.shortcuts import render,redirect
from testapp.models import EnquiryModel,Jobs,Apply
from testapp.forms import Enquiry,JobsForm,UserForm
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# Create your views here.
def home_view(request):
    return render(request,'testapp/home.html')
def python_view(request):
    return render(request,'testapp/python.html')
def java_view(request):
    return render(request,'testapp/java.html')
def enquiry_view(request):
	form=Enquiry()
	if request.method=='POST':
		form=Enquiry(request.POST)
		if form.is_valid:
			form.save()
			return submit_view(request)
	return render(request,'testapp/enquiry.html',{'form':form})
def register_view(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['username']
        first_name=request.POST['f_name']
        last_name=request.POST['l_name']
        password=request.POST['pwd']
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username Taken')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email Id Taken') 
            return redirect('register')  
        else:
            user=User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,password=password)
            user.save()    
            return redirect('login')
    else:
        return render(request,'testapp/register.html') 
def login_view(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credential')  
            return redirect('login')  
    else:
        return render(request,'testapp/login.html')  
def logout_view(request):
    auth.logout(request)
    return redirect('/')

def submit_view(request):
	return render(request,'testapp/thankyou.html')
def html_view(request):
	return render(request,'testapp/htmlfile.html')
def css_view(request):
	return render(request,'testapp/cssfile.html')
def django_view(request):
	return render(request,'testapp/djangofile.html')
def javascript_view(request):
	return render(request,'testapp/javascriptfile.html')
def bootstrap_view(request):
	return render(request,'testapp/bootstrapfile.html')
def php_view(request):
	return render(request,'testapp/php.html')
def history_view(request):
	return render(request,'testapp/history.html')
def feature_view(request):
	return render(request,'testapp/feature.html')
def sup_view(request):
	return render(request,'testapp/sup.html')
def wp_view(request):
	return render(request,'testapp/wp.html')
def basic_view(request):
	return render(request,'testapp/b.html')
def dt_view(request):
	return render(request,'testapp/dy.html')
def op_view(request):
	return render(request,'testapp/or.html')
def cf_view(request):
	return render(request,'testapp/if.html')
def cf2_view(request):
	return render(request,'testapp/ifelse.html')
def cf3_view(request):
    return render(request,'testapp/i4.html')
def cf4_view(request):
    return render(request,'testapp/f2.html')
def cf5_view(request):
    return render(request,'testapp/while2.html')
def break2(request):
    return render(request,'testapp/break2.html')
def continue2(request):
    return render(request,'testapp/continue2.html')
def str1(request):
    return render(request,'testapp/str1.html')
def str2(request):
    return render(request,'testapp/str2.html')
def str3(request):
    return render(request,'testapp/str3.html')
def list3(request):
    return render(request,'testapp/lists.html')
def tuple4(request):
    return render(request,'testapp/tuple1.html')
def set6(request):
    return render(request,'testapp/set6.html')
def dict2(request):
    return render(request,'testapp/dict4.html')
def func1(request):
    return render(request,'testapp/func1.html')
def func2(request):
    return render(request,'testapp/func2.html')
def func3(request):
    return render(request,'testapp/func3.html')
def func4(request):
    return render(request,'testapp/func4.html')
def func5(request):
    return render(request,'testapp/func5.html')
def module1(request):
    return render(request,'testapp/module1.html')
def module2(request):
    return render(request,'testapp/module2.html')
def module3(request):
    return render(request,'testapp/module3.html')
def pack2(request):
    return render(request,'testapp/pack2.html')
def f1(request):
    return render(request,'testapp/f1.html')
def f2(request):
    return render(request,'testapp/f4.html')
def excep2(request):
    return render(request,'testapp/excep2.html')
def excep4(request):
    return render(request,'testapp/excep4.html')
def excep6(request):
    return render(request,'testapp/excep6.html')
def excep8(request):
    return render(request,'testapp/excep8.html')
def class1(request):
    return render(request,'testapp/co.html')
def next(request):
    return render(request,'testapp/next1.html')
def next2(request):
    return render(request,'testapp/next2.html')
def next3(request):
    return render(request,'testapp/next3.html')
def next4(request):
    return render(request,'testapp/next4.html')
def next5(request):
    return render(request,'testapp/next5.html')
def next6(request):
    return render(request,'testapp/next6.html')
def polymorphism(request):
    return render(request,'testapp/polymorphism.html')
def astr(request):
    return render(request,'testapp/atr.html')
def pdbc1(request):
    return render(request,'testapp/pdbc.html')
def con4(request):
    return render(request,'testapp/pdbc2.html')
def con5(request):
    return render(request,'testapp/pdbc3.html')
def iter2(request):
    return render(request,'testapp/iter.html')
def gen(request):
    return render(request,'testapp/generator.html')
def decorator2(request):
    return render(request,'testapp/decorator2.html')
def closure2(request):
    return render(request,'testapp/closure2.html')
def expression2(request):
    return render(request,'testapp/expression2.html')
def next7(request):
    return render(request,'testapp/next7.html')
def search2(request):
    return render(request,'testapp/search2.html')
def thread1(request):
    return render(request,'testapp/thread1.html')
def next8(request):
    return render(request,'testapp/next8.html')
def tmod(request):
    return render(request,'testapp/tm2.html')
def st2(request):
    return render(request,'testapp/st2.html')
def sl2(request):
    return render(request,'testapp/sl2.html')
def vtm2(request):
    return render(request,'testapp/vtm2.html')
def ast2(request):
    return render(request,'testapp/ast2.html')
def json2(request):
    return render(request,'testapp/json2.html')
def csv2(request):
    return render(request,'testapp/csv2.html')
def dv2(request):
    return render(request,'testapp/dv2.html')
def pandas2(request):
    return render(request,'testapp/pandas2.html')
def numpy2(request):
    return render(request,'testapp/numpy2.html')
def pickling2(request):
    return render(request,'testapp/pickling2.html')
def unpickling2(request):
    return render(request,'testapp/unpickling2.html')
def doctyping2(request):
    return render(request,'testapp/doctyping2.html')
def contact2(request):
    return render(request,'testapp/contact2.html')
def about2(request):
    return render(request,'testapp/about2.html')
def jobs(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user:
            auth.login(request,user)
            return redirect('/job2')
        else:
            messages.info(request,'Invalid credential')  
            return redirect('login')  
    else:
        return render(request,'testapp/jobs.html')
    return render(request,'testapp/jobs.html')
def retrieve(request):
    job=Jobs.objects.all()
    return render(request,'testapp/job2.html',{'job':job})             
def apply(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        mobile=request.POST['mobile']
        birthday=request.POST['birthday']
        location=request.POST['location']
        designation=request.POST['designation']
        qualification=request.POST['qualification']
        language=request.POST['language']
        nationality=request.POST['nationality']
        year_of_passout=request.POST['year_of_passout']
        job_type=request.POST['job_type']
        current_ctc=request.POST['current_ctc']
        expected_ctc=request.POST['expected_ctc']
        gender=request.POST['gender']
        experience=request.POST['experience']
        form=Apply( Name=name,Email=email,Mobile=mobile,Gender=gender,Location=location,Designation=designation,DOB=birthday,Qualification=qualification,Experience=experience,Language=language,Nationality=nationality,year_of_passout=year_of_passout,job_type=job_type,current_ctc=current_ctc,expected_ctc=expected_ctc)
        form.save()
        messages.info(request,'Thanks for Applying!!! Welcome Our site')
        return redirect('/job2') 
    else:
        return redirect('/job2') 
def search(request):
    queryString=request.GET['q']
    job=Jobs.objects.filter(title__contains=queryString)
    return render(request,'testapp/job2.html',{'job':job})
def xpress(request):
    return render(request,'testapp/xpress.html')
def employer2(request):
    return render(request,'testapp/employer2.html')
@login_required
def create(request):
    form=JobsForm()
    if request.method=='POST':
        form=JobsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/job2')
    return render(request,'testapp/create.html',{'form':form})
def signup(request):
    form=UserForm()
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signup.html',{'form':form})
def logout2(request):
    return render(request,'testapp/logout2.html')
def program2(request):
    return render(request,'testapp/program2.html')
def fact2(request):
    return render(request,'testapp/fact2.html')
def fibonaci2(request):
    return render(request,'testapp/fibonaci2.html')
def arm2(request):
    return render(request,'testapp/arm2.html')
def even(request):
    return render(request,'testapp/even.html')
def add(request):
    return render(request,'testapp/add.html')
def minimum(request):
    return render(request,'testapp/minimum.html')
def prime(request):
    return render(request,'testapp/prime.html')
def polyndrome(request):
    return render(request,'testapp/polyndrome.html')
def findsalary(request):
    return render(request,'testapp/findsalary.html')