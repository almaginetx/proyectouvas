# Create your models here.
# -*- encoding: utf-8 -*-
import uuid
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from django.utils.timezone import now
import os
import random
from ckeditor_uploader.fields import RichTextUploadingField

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True)
    nickname = models.CharField(blank=True, max_length=200, verbose_name="nickname")
    phone = models.CharField(blank=True, max_length=200, verbose_name="teléfono")
    color = models.CharField(blank=True, max_length=200, verbose_name="color")
    password2 = models.CharField(blank=True, max_length=200, verbose_name="Password")
    avatar = models.ImageField(upload_to='userprofiles/avatar', blank=True, null=True)
    wallet = models.IntegerField(blank=True, null=True, default=0)
    verified = models.IntegerField(blank=True, null=True, default=0, verbose_name="¿Verificado?")
    admin = models.IntegerField(blank=True, null=True, default=0, verbose_name="¿Administrador?")
    create_at = models.DateTimeField(default=now, editable=False)
    update_at = models.DateTimeField(auto_now_add = False, auto_now=True, editable=False)
    slug = models.SlugField(editable=True)
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
    def __str__(self):
        return self.nickname
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.nickname)
        super(UserProfile, self).save(*args, **kwargs)

#Tracks

class Track(models.Model):
    title = models.TextField(blank=True, verbose_name="title")
    audio = models.FileField(upload_to='tracks/audio', blank=True, null=True)
    user = models.ForeignKey(User, related_name='track_user', blank=True, null=True)
    create_at = models.DateTimeField(default=now, editable=False)
    update_at = models.DateTimeField(auto_now_add = False, auto_now=True, editable=False)
    slug = models.SlugField(editable=False,max_length=144)

    def get_absolute_url(self):
        return reverse('blog.track', kwargs={'slug': self.slug})

    def extension_class(self):
        name, extension = os.path.splitext(self.audio.name)
        return extension

    class Meta:
            ordering = ['create_at']
            verbose_name = 'Audio'
            verbose_name_plural = 'Audios'

    def __unicode__(self):
        return self.title

    def save(self):
        super(Track, self).save()
        date = self.create_at
        self.slug = '%i-%i-%i-audio-%i' % (
            date.year, date.month, date.day, self.id
        )
        super(Track, self).save()

class Category(models.Model):
    title = models.CharField(max_length=300, verbose_name="Title")
    description = models.TextField(blank=True, verbose_name="Description")
    picture = models.ImageField(upload_to='categories', blank=True, null=True)
    create_at = models.DateTimeField(default=now, editable=False)
    update_at = models.DateTimeField(auto_now_add = False, auto_now=True, editable=False)
    slug = models.SlugField(editable=False)

    class Meta:
        ordering = ['create_at']
        verbose_name = "Tema"
        verbose_name_plural = 'Temas'

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

class Blog(models.Model):
    title = models.CharField(max_length=300, verbose_name="Title")
    description = RichTextUploadingField(blank=True, verbose_name="Description")
    picture = models.ImageField(upload_to='blogs', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Category-Blog")
    create_at = models.DateTimeField(default=now, editable=False)
    update_at = models.DateTimeField(auto_now_add = False, auto_now=True, editable=False)
    slug = models.SlugField(editable=False)

    class Meta:
        ordering = ['create_at']
        verbose_name = "Blog"
        verbose_name_plural = 'Blogs'

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

class Config(models.Model):
    title = models.CharField(max_length=300, verbose_name="Titulo")
    active = models.IntegerField(blank=True, null=True, default=1, verbose_name="¿Activado?")
    color = models.CharField(blank=True, max_length=300, verbose_name="Color")
    description = models.TextField(blank=True, verbose_name="Descripcion de portada")
    who = models.TextField(blank=True, verbose_name="Texto Quienes somos")
    tlf = models.CharField(blank=True, max_length=300, verbose_name="Texto de Teléfono")
    whatsapp = models.CharField(blank=True, max_length=300, verbose_name="Whatsapp")
    address = models.CharField(blank=True, max_length=300, verbose_name="Dirección")
    map = models.TextField(blank=True, verbose_name="Mapa de google")
    picture = models.ImageField(upload_to='config', blank=True, null=True,verbose_name="Foto de portada")
    create_at = models.DateTimeField(default=now, editable=False)
    update_at = models.DateTimeField(auto_now_add = False, auto_now=True, editable=False)
    slug = models.SlugField(editable=False)

    class Meta:
        ordering = ['create_at']
        verbose_name = "Proyecto"
        verbose_name_plural = 'Proyectos'

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Config, self).save(*args, **kwargs)
        
class Task(models.Model):
    title = models.TextField(blank=True, verbose_name="title")
    create_at = models.DateTimeField(default=now, editable=False)
    update_at = models.DateTimeField(auto_now_add = False, auto_now=True, editable=False)
    slug = models.SlugField(editable=False,max_length=144)

    class Meta:
        ordering = ['create_at']
        verbose_name = "Actualización"
        verbose_name_plural = 'Actualizaciones'

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Task, self).save(*args, **kwargs)

class Company(models.Model):
    title = models.TextField(blank=True, verbose_name="Titulo")
    description = models.TextField(blank=True, verbose_name="Descripción")
    cost = models.IntegerField(blank=True, null=True, default=350)
    create_at = models.DateTimeField(default=now, editable=False)
    update_at = models.DateTimeField(auto_now_add = False, auto_now=True, editable=False)
    slug = models.SlugField(editable=False,max_length=144)

    class Meta:
        ordering = ['create_at']
        verbose_name = "Empresa"
        verbose_name_plural = 'Empresas'

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Company, self).save(*args, **kwargs)
        
class Date(models.Model):
    title = models.CharField(max_length=300, verbose_name="Titulo")
    description = models.TextField(blank=True, verbose_name="Descripción")
    picture = models.ImageField(upload_to='dates', blank=True, null=True)
    start = models.DateTimeField(blank=True, null=True)
    finish = models.DateTimeField(blank=True, null=True)
    address = models.CharField(blank=True, max_length=600, verbose_name="Dirección")
    map = models.TextField(blank=True, verbose_name="Google Maps")
    active = models.IntegerField(blank=True, null=True, default=0, verbose_name="¿Principal?")
    owner = models.ForeignKey(UserProfile, related_name='evento_owner', blank=True, null=True, verbose_name="Usuario")
    create_at = models.DateTimeField(default=now, editable=False)
    update_at = models.DateTimeField(auto_now_add = False, auto_now=True, editable=False)
    slug = models.SlugField(editable=False)

    class Meta:
        ordering = ['create_at']
        verbose_name = "Evento"
        verbose_name_plural = 'Eventos'

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Date, self).save(*args, **kwargs)

class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name="Titulo")
    picture = models.ImageField(upload_to='dates', blank=True, null=True)
    price = models.IntegerField(blank=True, null=True, default=0, verbose_name="Precio en $COP")
    link = models.CharField(blank=True, max_length=3000, verbose_name="Link")
    pdf = models.FileField(upload_to='products/pdf', blank=True, null=True)
    create_at = models.DateTimeField(default=now, editable=False)
    update_at = models.DateTimeField(auto_now_add = False, auto_now=True, editable=False)
    slug = models.SlugField(editable=False)

    class Meta:
        ordering = ['create_at']
        verbose_name = "Producto"
        verbose_name_plural = 'Inventario'

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)
        
class Payment(models.Model):
    title = models.CharField(max_length=300, verbose_name="Banco")
    picture = models.ImageField(upload_to='payments', blank=True, null=True)
    link = models.CharField(blank=True, max_length=300, verbose_name="Link")
    country = models.CharField(blank=True, max_length=300, verbose_name="Pais")
    name = models.CharField(blank=True, max_length=300, verbose_name="Titular")
    accunttype = models.CharField(blank=True, max_length=300, verbose_name="Tipo de cuenta")
    account = models.CharField(blank=True, max_length=300, verbose_name="Numero de cuenta")
    govermentid = models.CharField(blank=True, max_length=300, verbose_name="Identificacion")
    mail = models.CharField(blank=True, max_length=300, verbose_name="Email")
    phone = models.CharField(blank=True, max_length=300, verbose_name="Telefono")
    address = models.CharField(blank=True, max_length=300, verbose_name="Direccion")
    description = models.TextField(blank=True, verbose_name="Notas adicionales")
    create_at = models.DateTimeField(default=now, editable=False)
    update_at = models.DateTimeField(auto_now_add = False, auto_now=True, editable=False)
    slug = models.SlugField(editable=False)

    class Meta:
        ordering = ['create_at']
        verbose_name = "Tipo de Pago"
        verbose_name_plural = 'Tipos de Pago'

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Payment, self).save(*args, **kwargs)
        
class Boucher(models.Model):
    title = models.CharField(max_length=300, verbose_name="Codigo")
    description = models.TextField(blank=True, verbose_name="Comentario")
    name = models.CharField(blank=True, max_length=300, verbose_name="Nombres y apellidos")
    tlf = models.CharField(blank=True, max_length=300, verbose_name="Teléfono")
    address = models.CharField(blank=True, max_length=300, verbose_name="Dirección")
    amount = models.CharField(blank=True, max_length=300, verbose_name="Monto pagado")
    picture = models.ImageField(upload_to='payments', blank=True, null=True)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Tipo de pago")
    owner = models.ForeignKey(UserProfile, related_name='payment_owner', blank=True, null=True, verbose_name="Usuario")
    create_at = models.DateTimeField(default=now, editable=False)
    update_at = models.DateTimeField(auto_now_add = False, auto_now=True, editable=False)
    slug = models.SlugField(editable=False)

    class Meta:
        ordering = ['create_at']
        verbose_name = "Recibo de pago"
        verbose_name_plural = 'Recibos de pago'

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Boucher, self).save(*args, **kwargs)
        
class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Producto")
    owner = models.ForeignKey(UserProfile, related_name='cart_owner', blank=True, null=True, verbose_name="Usuario")
    cant = models.IntegerField(blank=True, null=True, default=0, verbose_name="Cantidad")
    price = models.IntegerField(blank=True, null=True, default=0, verbose_name="Costo")
    create_at = models.DateTimeField(default=now, editable=False)
    update_at = models.DateTimeField(auto_now_add = False, auto_now=True, editable=False)
    slug = models.SlugField(editable=False)

    class Meta:
        ordering = ['create_at']
        verbose_name = "Articulos en carritos"
        verbose_name_plural = 'Carritos de compra'

    def __unicode__(self):
        return self.slug

    def save(self):
        super(Cart, self).save()
        date = self.create_at
        self.slug = '%i-%i-%i-cart-%i' % (
            date.year, date.month, date.day, self.id
        )
        super(Cart, self).save()
        
class Buyment(models.Model):
    buyment = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Usuario",related_name='buyment_owner')
    total = models.IntegerField(blank=True, null=True, default=0, verbose_name="Total a pagar")
    create_at = models.DateTimeField(default=now, editable=False)
    update_at = models.DateTimeField(auto_now_add = False, auto_now=True, editable=False)
    slug = models.SlugField(editable=False)

    class Meta:
        ordering = ['create_at']
        verbose_name = "Orden de compra"
        verbose_name_plural = 'Ordenes de compra'

    def __unicode__(self):
        return self.slug

    def save(self):
        super(Buyment, self).save()
        date = self.create_at
        self.slug = '%i-%i-%i-buyment-%i' % (
            date.year, date.month, date.day, self.id
        )
        super(Buyment, self).save()

def random_string():
        return str(random.randint(10000, 99999))
        
class Wallet(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Usuario",related_name='wallet_owner')
    total = models.FloatField(blank=True, null=True, default=0, verbose_name="Wallet")
    code = models.IntegerField(default = random_string)
    create_at = models.DateTimeField(default=now, editable=False)
    update_at = models.DateTimeField(auto_now_add = False, auto_now=True, editable=False)
    slug = models.SlugField(editable=False)

    class Meta:
        ordering = ['create_at']
        verbose_name = "INKACOIN Wallet"
        verbose_name_plural = 'INKACOIN Wallets'

    def __unicode__(self):
        return self.slug
    
    def save(self):
        super(Wallet, self).save()
        date = self.create_at
        codi = self.code
        codis = int(codi)
        strings = codis * codis
        cod = str(codi)
        string = str(strings)
        hashs = string + string
        hash = str(hashs)
        ikc = 'IKC'
        year = str(date.year)
        month = str(date.month)
        day = str(date.day)
        ids = str(self.id)
        variable = hash + cod + string + year + month + day + ids + ikc
        self.slug = slugify(variable)
        super(Wallet, self).save()
        
class Link(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Usuario",related_name='title_owner')
    total = models.FloatField(blank=True, null=True, default=0, verbose_name="Titled")
    code = models.IntegerField(default = random_string)
    link = models.CharField(default='link', max_length="1200")
    create_at = models.DateTimeField(default=now, editable=False)
    update_at = models.DateTimeField(auto_now_add = False, auto_now=True, editable=False)
    slug = models.SlugField(editable=False)

    class Meta:
        ordering = ['create_at']
        verbose_name = "INKACOIN LINK"
        verbose_name_plural = 'INKACOIN LINKS'

    def __unicode__(self):
        return self.slug
    
    def save(self):
        super(Link, self).save()
        date = self.create_at
        string = self.code * self.code
        hash = string + string
        self.slug = '%d-%i-%d-%i-%i-%i-%i-INKC' % (
            hash, self.code, string, date.year, date.month, date.day, self.id
        )
        super(Link, self).save()