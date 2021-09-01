from django.shortcuts import render,redirect
from .models import *
from random import *
from django.core.mail import send_mail
from django.conf import settings
import razorpay

# Create your views here.celler.


def SellerIndexpage(request):
    if 'id' in request.session:
        pk = seller.objects.get(id=request.session['id'])
        return render(request, "app/S-index.html",{'pk':pk})
    else:
        return redirect('login')

def Sellerloginpage(request):
    return render(request, "app/login.html")

def sellerregisterpage(request):
    return render(request, "app/register.html")

def sellerForgetpass(request):
    return render(request, "app/forgetpas.html")

def selleraddproduct(request):
    return render(request, "app/addproduct.html")

def Sellermyprofile(request):
    if 'id' in request.session:
        getusr = seller.objects.get(id=request.session['id'])
        return render(request,"app/Sellermyprofile.html",{'s':getusr})
    else:
        return redirect('login')

def s_updateprofile(request):
    if 'id' in request.session:
        pro = seller.objects.get(id=request.session['id'])
        pro.Shop_name = request.POST['fname'] if request.POST['fname'] else pro.Shop_name
        pro.Sname = request.POST['lname'] if request.POST['lname'] else pro.Sname
        pro.email = request.POST['email'] if request.POST['email'] else pro.email
        pro.mobile = request.POST['phnb'] if request.POST['phnb'] else pro.mobile
        pro.address = request.POST['add'] if request.POST['add'] else pro.address
        pro.save()
        return redirect("sellermyprofile")
    else:
        return redirect("login")

def pay(request):
    if request.method == "POST":
        name = int(request.POST['amt'])
        amount = name*100
        request.session['amt'] = amount

        client = razorpay.Client(
            auth=("rzp_test_4He88pida9ia21", "4uWDzZczk3bGni5X7rRetWnS"))

        payme = client.order.create({'amount': amount, 'currency': 'INR','payment_capture': '1'})
        
        return render(request, 'HR_app/payment.html')
    else:
        mag : "Error"
        return render(request, 'HR_app/hr-table-expense.html',{'err':mag})

def EmailVerificationPage(request):
    if request.method=='POST':
        emailid=request.POST["email"]
        user=seller.objects.filter(email=emailid)
        if len(user)>0:
            did=seller.objects.get(email=emailid)
            sbj="forgot your password"
            otp=""
            for i in range(6):
                otp+=str(randint(1,9))
            did.OTP =otp
            did.save()
            msg=f"your otp is {otp}"
            sender=settings.EMAIL_HOST_USER
            rl=[emailid,]
            # send_mail(sbj,msg,sender,rl)
            return render(request,"app/otp.html",{'em':emailid})
        else:
            err="Incorrect Email Id"
            return render(request,"app/forgetpas.html", {'msg': err})
    else:
        return render(request,"app/forgetpas.html")

def OTP_verify(request):
    if request.method=="POST":
        emailid=request.POST["email"]
        otp1=request.POST["sotp"]
        did=seller.objects.get(email=emailid)
        if did.OTP == otp1:
            return render(request,"app/changepass.html",{'data':did})
        else:
            err="Incorect OTP"
            return render(request,"app/otp.html",{'msg':err,'em':emailid})

def ChangePassword(request):
    if request.method=="POST":
        emailid=request.POST["email"]
        newpswd=request.POST["password"]
        repeatpswd=request.POST["newpswd"] 
        did=seller.objects.get(email=emailid)
        if newpswd == repeatpswd:
            did.Password = newpswd
            did.save()
            return redirect('login')
        return render(request,"app/changepass.html")
    else:
        return render(request,"app/otp.html")
    
def regseller(request):
    if request.method == 'POST':
        fn = request.POST['fname']
        ln = request.POST['lname']
        em = request.POST['email']
        ph = request.POST['phnb']
        adrs = request.POST['add']
        pwd = request.POST['pwd']

        slr = seller.objects.create(Shop_name=fn,Sname=ln,email=em,mobile=ph,address=adrs,passwd=pwd)
        return redirect("login")
    else:
        msg = ""
        return render(request, "app/register.html",{'err':msg})

def LogSeller(request):
    if request.method == 'POST':
        em = request.POST['email']
        pwd = request.POST['pwd']

        user = seller.objects.filter(email=em)
    
        if len(user) > 0:
            if user[0].passwd == pwd:
                request.session['id'] = user[0].id
                request.session['sname'] = user[0].Sname 
                request.session['email'] = user[0].email
                user=seller.objects.get(id=request.session['id'])
                return redirect("index")
            else:
                msg = "password is incorrect..!"
                return render(request, "app/login.html",{'err':msg})
        else:
            err="user doesn't exist !"
            return render(request,"app/login.html",{'msg':err})
    else:
        return redirect("login")


def Logout(request):
    try:
        del request.session['id']
        del request.session['sname']
        del request.session['email']
        return redirect('login')
    except:
        return redirect('login')

def addpro(request):
    if request.method == 'POST':
        pn = request.POST['pname']
        pim = request.FILES['proimg']
        pcat = request.POST['Pcat']
        pr = request.POST['Pprice']

        cat = category.objects.get(pcategory=pcat)
        Pro = product.objects.create(
            pro_name=pn,
            pro_image=pim,
            pro_category=cat,
            pro_price=pr
            )
        return redirect("allproduct")
    else:
        pass

def AllProduct(request):
    show=product.objects.all()
    return render(request,"app/allproduct.html",{'show':show})

def sellerdelete(request,pk):
    pro =  product.objects.get(id=pk)
    pro.delete()
    return redirect("allproduct")

def sellerorder(request):
    return render(request,"app/sellerorder.html")

# user side

def uIndexpage(request):
    show = product.objects.all()
    return render(request, "app/uindex.html",{'show':show})

def uLoginpage(request):
    return render(request, "app/ulogin.html")

def uRegisterpage(request):
    return render(request, "app/uregister.html")

def uForgetpass(request):
    return render(request, "app/uforgetpas.html")

def uaddcart(request):
    return render(request, "app/useraddcart.html")

def useraddcart(request,pk):
    if 'uid' in request.session:
        data= product.objects.get(id=pk)
        usr = User.objects.get(id=request.session['uid'])

        crt=AddCart.objects.create(prod=data,usrg=usr)

        return redirect('uindex')
    else:
        return redirect('ulogin') 
  
def uViewcart(request):
    if 'uid' in request.session:
        # usr = User.objects.get(id=request.session['uid'])
        ca = AddCart.objects.filter(usrg=request.session['uid'])
        return render(request, "app/uviewcart.html",{'ca':ca})
    else:
        return redirect('uindex') 

def uCheckout(request):
    return render(request, "app/usercheckout.html")

def userremove(request,pk):
    rem =  AddCart.objects.get(id=pk)
    rem.delete()
    return redirect("uviewcart")


def updatecart(request):
    return render(request,"app/userupdatecart.html")
    

# def updatecart(request):
#     if 'uid' in request.session:
#         ca = AddCart.objects.filter(usrg=request.session['uid'])
#         return render(request,"app/userupdatecart.html",{'ca:ca}'})
#     else:
#         return redirect('uindex')


def usermyprofilePage(request):
    if 'uid' in request.session:
        us = User.objects.get(id=request.session['uid'])
        return render(request,"app/usermyprofile.html",{'u':us}) 
    else:
        return redirect('ulogin')



def u_updateprofile(request):
    if 'iid' in request.session:
        usr = User.objects,get(id=request.session['uid'])
        usr.fname = request.post['fname'] if request.POST['fname'] else usr.fname
        usr.lname = request.POST['lname'] if request.POST['lname'] else usr.lname
        usr.email = request.POST['email'] if request.POST['email'] else usr.email
        usr.mobile = request.POST['phnb'] if request.POST['phnb'] else usr.mobile
        usr.address = request.POST['add'] if request.POST['add'] else usr.address
        usr.save()
        return redirect("uupdateprofile")
    else:
        return redirect("ulogin")


def uLoguser(request):
    if request.method == 'POST':
        em = request.POST['email']
        pwd = request.POST['pwd']

        user = User.objects.filter(email=em)
    
        if len(user) > 0:
            if user[0].passwd == pwd:
                request.session['uid'] = user[0].id
                request.session['ufname'] = user[0].fname 
                request.session['uemail'] = user[0].email
                return redirect("uindex")
            else:
                msg = "password is incorrect..!"
                return render(request, "app/ulogin.html",{'err':msg})
        else:
            err="user doesn't exist !"
            return render(request,"app/ulogin.html",{'msg':err})
    else:
        return redirect("ulogin")

def uReguser(request):
    if request.method == 'POST':
        fn = request.POST['fname']
        ln = request.POST['lname']
        em = request.POST['email']
        ph = request.POST['phnb']
        adrs = request.POST['add']
        pwd = request.POST['pwd']

        slr = User.objects.create(fname=fn,lname=ln,email=em,mobile=ph,address=adrs,passwd=pwd)
        return redirect("ulogin")
    else:
        msg = ""
        return render(request, "app/uregister.html",{'err':msg})


def uEmailVerificationPage(request):
    if request.method=='POST':
        emailid=request.POST["email"]
        user=User.objects.filter(email=emailid)
        if len(user)>0:
            did=User.objects.get(email=emailid)
            sbj="forgot your password"
            otp=""
            for i in range(6):
                otp+=str(randint(1,9))
            did.OTP =otp
            did.save()
            msg=f"your otp is {otp}"
            sender=settings.EMAIL_HOST_USER
            rl=[emailid,]
            send_mail(sbj,msg,sender,rl)
            return render(request,"app/uotp.html",{'em':emailid})
        else:
            err="Incorrect Email Id"
            return render(request,"app/uforgetpas.html", {'msg': err})
    else:
        return render(request,"app/uforgetpas.html")

def uOtpverify(request):
    if request.method=="POST":
        emailid=request.POST["email"]
        otp1=request.POST["sotp"]
        did=User.objects.get(email=emailid)
        if did.OTP == otp1:
            return render(request,"app/uchangepass.html",{'data':did})
        else:
            err="Incorect OTP"
            return render(request,"app/uotp.html",{'msg':err,'em':emailid})

def uChangepassword(request):
    if request.method=="POST":
        emailid=request.POST["email"]
        newpswd=request.POST["password"]
        repeatpswd=request.POST["newpswd"] 
        did=User.objects.get(email=emailid)
        if newpswd == repeatpswd:
            did.Password = newpswd
            did.save()
            return redirect('ulogin')
        return render(request,"app/uchangepass.html")
    else:
        return render(request,"app/uotp.html")
    

def uLogout(request):
    del request.session['uid']
    del request.session['ufname']
    del request.session['uemail']
    return redirect('uindex')


# def uAllproduct(request):
#     show=product.objects.all()
#     return render(request,"app/uallproduct.html",{'show':show})






