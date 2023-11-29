from django import forms
from farmapp.models import Products, ImageModel, Order, Contact, Subscriber, Blog_single, Appointment


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'price', 'description', 'type']

class ImagesUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['image', 'title', 'price']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'email', 'phone', 'date', 'message']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject',  'message']

class Blog_singleForm(forms.ModelForm):
    class Meta:
        model = Blog_single
        fields = ['name', 'email', 'website',  'comment']

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'phone', 'date', 'department', 'message']



