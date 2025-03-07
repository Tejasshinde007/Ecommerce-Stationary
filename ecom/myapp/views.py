from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Product,Cart,Address,Order
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout
import re
import random
import razorpay
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.timezone import now
# Create your views here.

def home(request):
    return render(request,"home.html")

def aboutus(request):
    return render(request,"aboutus.html")

def shop(request):
    return render(request,'books.html')

def cart(request):
    return render(request,'cart.html')


def storybook(request,cid):
    context={}
    story=Product.objects.filter(category=cid)
    context['storybook']=story
    return render(request,'storybooks.html',context)

def biography(request,cid):
    context={}
    bio=Product.objects.filter(category=cid)
    context['biography']=bio
    return render(request,'biography.html',context)

def lkgukg(request,cid):
    context={}
    lkg=Product.objects.filter(category=cid)
    context['lkgukg']=lkg
    return render(request,'lkgukg.html',context)

def firsttofifth(request,cid):
    context={}
    first=Product.objects.filter(category=cid)
    context['firsttofifth']=first
    return render(request,'firsttofifth.html',context)

def sixthtotenth(request,cid):
    context={}
    ten=Product.objects.filter(category=cid)
    context['sixthtotenth']=ten
    return render(request,'sixthtotenth.html',context)

def writtinginstruments(request,cid):
    context={}
    write=Product.objects.filter(category=cid)
    context['writting']=write
    return render(request,'writtinginstrument.html',context)


def ulogin(request):
    context={}
    if request.method=="POST":
        un=request.POST["uname"]
        p=request.POST["upass"]
        # print(un,p)
        if un=="" or p=="":
            context['error_msg']="All fields are required"
            return render(request,"login.html",context)
        else:
            u=authenticate(username=un,password=p)
            print(u)
            if u!=None:
                login(request,u)
                return redirect("/")
            else:
                context["error_msg"]="Invalid Username and password"
                return render(request,"login.html",context)
            
    return render(request,"login.html")

def register(request):
    context={}
    if request.method=="POST":
        un=request.POST["uname"]
        e=request.POST["uemail"]
        fn=request.POST["fname"]
        ln=request.POST["lname"]
        p=request.POST["upass"]
        cp=request.POST["cppass"]
        print(un,e,p,cp,fn,ln)
        if un=="" or e=="" or p=="" or cp=="" or fn=="" or ln=="":
            context['error_msg']="All fields are required"
            return render(request,"register.html",context)
        
        elif not re.match(r"^[a-zA-Z0-9_.@-]{3,20}$", un):
            context['error_msg'] = "Username must be 3-20 characters long and can include letters, numbers, underscores (_), hyphens (-), periods (.), and at symbol (@)"
            return render(request, "register.html", context)
        
        elif not re.match(r"^[A-Za-z]{2,}$", fn):
            context['error_msg'] = "First name must contain only letters and be at least 2 characters long"
            return render(request, "register.html", context)
        
        elif not re.match(r"^[A-Za-z]{2,}$", ln):
            context['error_msg'] = "Last name must contain only letters and be at least 2 characters long"
            return render(request, "register.html", context)
        
        elif not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", e):
            context['error_msg'] = "Invalid email format"
            return render(request, "register.html", context)
        
        elif not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]).{8,}$", p):
            context['error_msg'] = "Password must be at least 8 characters long, include at least one uppercase letter, one lowercase letter, one digit, and one special character."
            return render(request, "register.html", context)
        
        elif p!=cp:
            context['error_msg']="Password Dosent match"
            return render(request,"register.html",context)
        
        elif len(p)< 8:
            context["error_msg"]="Password contain atlest 8 character"
            return render(request,"register.html",context)
        else:
            user=User.objects.create(username=un,email=e,first_name=fn,last_name=ln)
            user.set_password(p)
            user.save()
            return redirect('/login')
        
        
    else:
        return render(request,"register.html")
    

def ulogout(request):
    logout(request)
    return redirect("/login")

def addtocart(request,pid):
    context={}
    product=Product.objects.filter(id=pid)
    context['product']=product
    if request.user.is_authenticated:
        u=User.objects.filter(id=request.user.id)  
        p=Product.objects.filter(id=pid)
        print(u[0],p[0])
        q1=Q(userid=u[0])     
        q2=Q(pid=p[0])       
        cart=Cart.objects.filter(q1 & q2)   
        if len(cart)==1:                   
            context['error_msg']="Product already exist in cart"
            return render(request,'product.html',context)
        else:
            cart=Cart.objects.create(userid=u[0],pid=p[0])
            cart.save()
            context['success']="Product added to cart successfully !!!"
            # print(cart)
            return render(request,'product.html',context)
    else:                               
        context['error_msg1']="Please login first"    
        return render(request,'product.html',context)

def product_details(request,pid):
    context={}
    prod=Product.objects.filter(id=pid)
    context['product']=prod
    return render(request,"product.html",context)


   

 
def viewcart(request):
    context={}
    carts=Cart.objects.filter(userid=request.user.id)
    
    saving_amt=0
    total_amt=0
    items=0
    for cart in carts:
        saving_amt+=(cart.pid.price - cart.pid.offer_price) * cart.qty  
        total_amt+=cart.pid.offer_price * cart.qty  
        items+=cart.qty     
   
    context['saving']=saving_amt
    context['total']=total_amt
    context['items']=items    
     
    
    if len(carts)==0:
        context['text']="No items in cart"
        return render(request,"cart.html",context)
    else:
        context['carts']=carts
        return render(request,"cart.html",context)

def deletecart(request,cid):
    cart=Cart.objects.filter(id=cid)
    cart.delete()
    return redirect('/cart')

def updateqty(request,x,cid):
    cart=Cart.objects.filter(id=cid)
    quantity=cart[0].qty
    if x=='1':
        quantity+=1
    elif quantity > 1:
        quantity-=1
    cart.update(qty=quantity)
    return redirect('/cart')

def checkaddress(request):
    context={}
    u=User.objects.filter(id=request.user.id)
    add=Address.objects.filter(user_id=u[0])
    if len(add) >=1:
        return redirect('/placeorder')
    else:
        if request.method=="POST":
            fn=request.POST["full_name"]
            ad=request.POST["address"]
            ct=request.POST["city"]
            st=request.POST["state"]
            zp=request.POST["zipcode"]
            mob=request.POST["mobile"]
            if not all([fn, ad, ct, st, zp, mob]):
                context['error_msg'] = "All fields are required."
                return render(request, "address.html", context)

            # Validate full name (only letters and spaces allowed)
            if not re.fullmatch(r"[A-Za-z\s]+", fn):
                context['error_msg'] = "Full Name must contain only alphabets."
                return render(request, "address.html", context)

            # Validate mobile number (10-digit, starting with 6-9)
            if not re.fullmatch(r"[6-9]\d{9}", mob):
                context['error_msg'] = "Invalid Mobile Number. Enter a valid 10-digit number."
                return render(request, "address.html", context)

            # Validate pincode (6-digit numeric)
            if not re.fullmatch(r"\d{6}", zp):
                context['error_msg'] = "Invalid Zipcode. It should be a 6-digit number."
                return render(request, "address.html", context)
            
            else:
                address=Address.objects.create(user_id=u[0],fullname=fn,address=ad,city=ct,state=st,pincode=zp,mobile=mob)
                address.save()
                return redirect('/placeorder')
                
            
        
        else:
            return render(request,"address.html")

def placeorder(request):
    carts=Cart.objects.filter(userid=request.user.id)
    for i in carts:
        oid=random.randint(1111,9999)  
        totalamt=i.pid.offer_price*i.qty   
        order=Order.objects.create(order_id=oid,user_id=i.userid,p_id=i.pid,amt=totalamt,qty=i.qty)  
        order.save()
    return redirect('/fetchorder')
        

def fetchorder(request):
    context={}
   
    u=User.objects.filter(id=request.user.id)
    carts=Cart.objects.filter(userid=request.user.id)
    address=Address.objects.filter(user_id=u[0])
    q1=Q(user_id=u[0])
    q2=Q(payment_status="unpaid")
    orders=Order.objects.filter(q1&q2)
    
    saving_amt=0
    total_amt=0
    items=0
    for cart in carts:
        saving_amt+=(cart.pid.price - cart.pid.offer_price) * cart.qty  
    for i in orders:
        total_amt+=i.amt
        items+=i.qty
    context['saving']=saving_amt
    context['total']=total_amt
    context['items']=items 
   
    context['address']=address
    context['carts']=carts
    
    return render(request,"placeorder.html",context)

def makepayment(request):
    context={}
    u=User.objects.filter(id=request.user.id)
    carts=Cart.objects.filter(userid=request.user.id)
    client=razorpay.Client(auth=("rzp_test_WbIobfpNgPbwWC","GIPFE5y9tfnQKAPjGMMSD30n")) 
   
    q1=Q(user_id=u[0])
    q2=Q(payment_status="unpaid")
    orders=Order.objects.filter(q1&q2)
    sum=0
    saving_amt=0
    items=0
    for order in orders:
        sum+=order.amt
        orderid=order.order_id
        items+=order.qty
    for cart in carts:
        saving_amt+=(cart.pid.price - cart.pid.offer_price) * cart.qty
    print(sum)
    data={"amount":sum*100,"currency":"INR","receipt":orderid}
    payment=client.order.create(data=data)
    context["payment"]=payment
    context["orders"]=orders
    context['total']=sum
    context['saving']=saving_amt
    context['items']=items
    return render(request,'pay.html',context)


def email_send(request):
    user_email = request.user.email  
    u=User.objects.filter(id=request.user.id)
   
    q1=Q(user_id=u[0])
    q2=Q(payment_status="paid")
    paidorders=Order.objects.filter(q1&q2).order_by('-payment_date')
    
    if not paidorders.exists():
        return redirect('/update_order_status')  

   
    subject = "Your Order History"
    from_email = "tejasshinde5156@gmail.com"

   
    message = render_to_string('email.html', {
        'customer_name': request.user.username,  
        'orders': paidorders  
        
    })

   
    email = EmailMessage(subject, message, from_email, [user_email])
    email.content_subtype = "html"  
    email.send()

    return redirect('/update_order_status')

def update_order_status(request):
    u=User.objects.filter(id=request.user.id)
    q1=Q(user_id=u[0])
    q2=Q(payment_status="unpaid")
    orders=Order.objects.filter(q1&q2)
    orders.update(payment_status="paid",payment_date=now())
    
    return redirect("/")

def search(request):
    context={}
    query=request.GET['query']
    s=Product.objects.filter(pname__icontains=query)
    context["search"]=s
    return render(request,"search.html",context)

def userinfo(request):
    context = {"profile": [request.user]}  
    return render(request, "profile.html", context)


def delete_user(request, uid):
    if request.user.id == uid: 
        u=User.objects.get(id=request.user.id)
        u.delete()
        print("deleted user")
        return redirect("/register")
    else:
        return redirect("/")

def myorder(request):
    context = {}
    paid_orders = Order.objects.filter(user_id=request.user.id)
   
    context["orderpaid"] = paid_orders

    return render(request, "myorder.html", context)