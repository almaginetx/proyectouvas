# Create your forms here.
# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, Track, Payment, Boucher, Category, Blog
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class signup_form(forms.Form):
    username = forms.EmailField(
        label='Correo electrónico',
        min_length=1,
        widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(
        label='Teléfono',
        min_length=1,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    nickname = forms.CharField(
        label='Nombre de usuario',
        min_length=1,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        label='Cree una contraseña segura',
        min_length=3,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(
        label='Repita la contraseña',
        min_length=3,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    def clean_username(self):
        """Comprueba que no exista un username igual en la db"""
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError('Este Correo ya se encuentra registrado')
        return username
    def clean_nickname(self):
        """Comprueba que no exista un email igual en la db"""
        nickname = self.cleaned_data['nickname']
        if UserProfile.objects.filter(nickname=nickname):
            raise forms.ValidationError('Este nombre de usuario ya existe')
        return nickname
    def clean_password2(self):
        """Comprueba que password y password2 sean iguales."""
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('Las contraseñas deben ser iguales')
        return password2

class uploadtrack_form(forms.Form):
    title = forms.CharField(
        label='Titulo de su audio',
        widget=forms.Textarea(attrs={'class': 'form-control'}))
    audio = forms.FileField(
        label='Seleccione un nuevo audio')

class updateavatar_form(forms.Form):
    avatar = forms.FileField(
        label='Foto')
        
class updatenickname_form(forms.Form):
    nickname = forms.CharField(
        label='Su nuevo nombre de usuario',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
        
class payment_form(forms.Form):
    payment = forms.ModelChoiceField(
        queryset=Payment.objects.all(),label="Tipo de pago",required=True)
    title = forms.CharField(
        label='Numero de comprobante de pago',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    amount = forms.CharField(
        label='Monto pagado',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(
        label='Nombres y apellidos',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    tlf = forms.CharField(
        label='Número de Teléfono',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(
        label='Dirección, Ciudad y País',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    picture = forms.FileField(
        label='Opcional, foto del comprobante',
        required=False,)
    description = forms.CharField(
        label='Comentarios adicionales',
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control'}))
        
class paymentc_form(forms.Form):
    payment = forms.ModelChoiceField(
        queryset=Payment.objects.all(),label="Tipo de pago",required=True)
    title = forms.CharField(
        label='Numero de comprobante de pago',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    amount = forms.CharField(
        label='Monto pagado',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(
        label='Nombres y apellidos',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    tlf = forms.CharField(
        label='Número de Teléfono',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(
        label='Dirección, Ciudad y País',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    picture = forms.FileField(
        label='Opcional, foto del comprobante',
        required=False,)
    description = forms.CharField(
        label='Comentarios adicionales',
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control'}))
        
class createblog_form(forms.Form):
    title = forms.CharField(
        label='Título de su publicación',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),label="Categoría",required=True)
    picture = forms.FileField(
        label='Foto de la publicación',
        required=True,)
    description = forms.CharField(
        label='Contenido de la publicación',
        required=True,
        widget=CKEditorUploadingWidget())