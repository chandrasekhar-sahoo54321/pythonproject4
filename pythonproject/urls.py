"""pythonproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testapp import views
from django.conf.urls import url,include 

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.home_view),
    url(r'^python/',views.python_view),
    url(r'^java/',views.java_view),
    url(r'^enquiry/',views.enquiry_view),
    url(r'^thank/',views.submit_view),
    url(r'^html/',views.html_view),
    url(r'^css/',views.css_view),
    url(r'^django/',views.django_view),
    url(r'^javascript/',views.javascript_view),
    url(r'^bootstrap/',views.bootstrap_view),
    url(r'^php/',views.php_view),
    url(r'^history/',views.history_view),
    url(r'^feature/',views.feature_view),
    url(r'^sup/',views.sup_view),
    url(r'^wp/',views.wp_view),
    url(r'^b/',views.basic_view),
    url(r'^da/',views.dt_view),
    url(r'^or/',views.op_view),
    url(r'^if/',views.cf_view),
    url(r'^if2/',views.cf2_view),
    url(r'^i4/',views.cf3_view),
    url(r'^f2/',views.cf4_view),
    url(r'^while2/',views.cf5_view),
    url(r'^break/',views.break2),
    url(r'^continue2/',views.continue2),
    url(r'^str1/',views.str1),
    url(r'^str2/',views.str2),
    url(r'^str3/',views.str3),
    url(r'^lst/',views.list3),
    url(r'^tuple1/',views.tuple4),
    url(r'^set6/',views.set6),
    url(r'^dict2/',views.dict2),
    url(r'^func1/',views.func1),
    url(r'^func2/',views.func2),
    url(r'^func3/',views.func3),
    url(r'^func4/',views.func4),
    url(r'^func5/',views.func5),
    url(r'^module1/',views.module1),
    url(r'^module2/',views.module2),
    url(r'^module3/',views.module3),
    url(r'^pack2/',views.pack2),
    url(r'^f1/',views.f1),
    url(r'^f4/',views.f2),
    url(r'^exc/',views.excep2),
    url(r'^exc2/',views.excep4),
    url(r'^exc4/',views.excep6),
    url(r'^exc8/',views.excep8),
    url(r'^class1/',views.class1),
    url(r'^next1/',views.next),
    url(r'^next2/',views.next2),
    url(r'^next3/',views.next3),
    url(r'^next4/',views.next4),
    url(r'^next5/',views.next5),
    url(r'^next6/',views.next6),
    url(r'^ph/',views.polymorphism),
    url(r'^astr/',views.astr),
    url(r'^pdbc1/',views.pdbc1),
    url(r'^pdbc2/',views.con4),
    url(r'^pdbc3/',views.con5),
    url(r'^iter/',views.iter2),
    url(r'^gtr/',views.gen),
    url(r'^decor/',views.decorator2),
    url(r'^closure2/',views.closure2),
    url(r'^expression2/',views.expression2),
    url(r'^next7/',views.next7),
    url(r'^search2/',views.search2),
    url(r'^thread1/',views.thread1),
    url(r'^next8/',views.next8),
    url(r'^tmod/',views.tmod),
    url(r'^st2/',views.st2),
    url(r'^sl2/',views.sl2),
    url(r'^vtm2/',views.vtm2),
    url(r'^ast2/',views.ast2),
    url(r'^json2/',views.json2),
    url(r'^csv2/',views.csv2),
    url(r'^dv2/',views.dv2),
    url(r'^pandas2/',views.pandas2),
    url(r'^numpy2/',views.numpy2),
    url(r'^pickling2/',views.pickling2),
    url(r'^unpickling2/',views.unpickling2),
    url(r'^doctyping2/',views.doctyping2),
    url(r'^contact2/',views.contact2),
    url(r'^about2/',views.about2),
    url(r'^jobs/',views.jobs),
    url(r'^job2/',views.retrieve),
    url(r'^apply/',views.apply),
    url(r'^search/',views.search),
    url(r'^xpress/',views.xpress),
    url(r'^em/',views.employer2),
    url(r'^create/',views.create),
    url(r'^accounts/',include('django.contrib.auth.urls')),
    url(r'^sign/',views.signup),
    url(r'^logout2/',views.logout2),
    url(r'^program/',views.program2),
    url(r'^fact/',views.fact2),
    url(r'^fibo/',views.fibonaci2),
    url(r'^arm/',views.arm2),
    url(r'^even/',views.even),
    url(r'^add/',views.add),
    url(r'^minimum/',views.minimum),
    url(r'^prime/',views.prime),
    url(r'^polyndrome/',views.polyndrome),
    url(r'^findsalary/',views.findsalary),
    url(r'^register/',views.register_view,name='register'),
    url(r'^login/',views.login_view,name='login'),
    url(r'^logout/',views.logout_view,name='logout')



]
