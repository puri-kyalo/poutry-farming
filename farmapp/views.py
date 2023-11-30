import json

import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from requests.auth import HTTPBasicAuth


from farmapp.forms import ProductsForm, ImagesUploadForm, ContactForm, SubscribeForm, Blog_singleForm, AppointmentForm
from farmapp.models import Member, Products, ImageModel
from farmapp.forms import OrderForm
from farmapp.credentials import MpesaC2bCredential, MpesaAccessToken, LipanaMpesaPpassword


# Create your views here.
def register(request):
    if request.method == 'POST':
        member = Member(firstname=request.POST['firstname'], lastname=request.POST['lastname'],
                        email=request.POST['email'], username=request.POST['username'],
                        password=request.POST['password'])
        member.save()
        return redirect('/')
    else:
        return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def index(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'],
                                 password=request.POST['password'],).exists():
            member = Member.objects.get(username=request.POST['username'],password=request.POST['password'],)
            return render(request, 'index.html', {'member': member})
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def about(request):
    return render(request, 'about.html')

def team(request):
    return render(request, 'team.html')

def testmonials(request):
    return render(request, 'testimonials.html')

def gallery(request):
    return render(request, 'gallery.html')

def services(request):
    return render(request, 'services.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def portfoliodetails(request):
    return render(request, 'portfolio-details.html')

def pricing(request):
    return render(request, 'pricing.html')

def blog(request):
    return render(request, 'blog.html')

def blog_single(request):
    if request.method == "POST":
        form = Blog_singleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/blog_single")
    else:
        form = ContactForm()
    return render(request, 'blog_single.html', {'form': form})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/contact")
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})



def order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/order")
    else:
        form = OrderForm()
    return render(request, 'order.html', {'form': form})

def products(request):
    if request.method == "POST":
        form = ProductsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/display")
    else:
        form = ProductsForm()
    return render(request, 'products.html', {'form': form})

def display(request):
    products = Products.objects.all()
    return render(request, 'display.html', {'products': products})

def delete(request, id):
    product = Products.objects.get(id=id)
    product.delete()
    return redirect('/display')

def edit(request, id):
    product = Products.objects.get(id=id)
    return render(request, 'edit.html', {'product': product})

def update(request, id):
    product = Products.objects.get(id=id)
    form = ProductsForm(request.POST, instance=product)
    if form.is_valid():
        form.save()
        return redirect('/display')
    else:
        return render(request, 'edit.html', {'product':product})

def token(request):
    consumer_key = 'USTR7PnePw7ewYcTsBA3IjPAHoAKega3'
    consumer_secret = '7BKY8qDITDmdmT3y'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token": validated_mpesa_access_token})

def m_payment(request):
    return render(request, 'm_payment.html')

def stk(request):
    if request.method == "POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Apen Softwares",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("Success")

def upload_image(request):
    if request.method == 'POST':
        form = ImagesUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/image')
    else:
        form = ImagesUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'show_image.html', {'images': images})

def imagedelete(request, id):
    image = ImageModel.objects.get(id=id)
    image.delete()
    return redirect('/image')

def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            # You can add additional logic here, like sending a confirmation email
            return redirect('/subscribe')  # Redirect to a success page
    else:
        form = SubscribeForm()

    return render(request, 'subscribe.html', {'form': form})

def appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/appointment")
    else:
        form = AppointmentForm()
    return render(request, 'appointment.html', {'form': form})
