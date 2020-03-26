# Create your view here.
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest, HttpResponse, HttpRequest, HttpResponseRedirect
from django.core import serializers
from django.shortcuts import redirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django.conf import settings
from .forms import *
from .models import *
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.utils import timezone
import re
from django.db.models import Q
from django.core.context_processors import csrf
from django import forms 
from django.middleware.csrf import CsrfViewMiddleware, get_token
from django.utils.decorators import available_attrs, decorator_from_middleware
from django.template import RequestContext

#API REST
from django.db.models.query import QuerySet
import json
from django.views.generic.list import ListView

def login_view(request):
    # Si el usuario esta ya logueado, lo redireccionamos a index_view
    if request.user.is_authenticated():
        return redirect(reverse('app.welcome'))
    message = ''
    userprofile = UserProfile.objects.all().order_by('-create_at')
    track = Track.objects.all().order_by('-create_at')
    category = Category.objects.all().order_by('-create_at')[:3]
    categorys = Category.objects.all().order_by('-create_at')
    blog = Blog.objects.all().order_by('-create_at')
    product = Product.objects.all().order_by('-create_at')
    payment = Payment.objects.all().order_by('-create_at')
    now = timezone.now()
    config = Config.objects.get(active = 1)
    date = Date.objects.get(active = 1)
    template = 'app/login.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('app.login'))
            else:
                # Redireccionar informando que la cuenta esta inactiva
                # Lo dejo como ejercicio al lector :)
                pass
        message = 'Datos de ingreso incorrectos. Intente de nuevo'
    return render_to_response(template,locals(),context_instance=RequestContext(request))

def logins_view(request):
    # Si el usuario esta ya logueado, lo redireccionamos a index_view
    if request.user.is_authenticated():
        return redirect(reverse('app.welcome'))
    message = ''
    userprofile = UserProfile.objects.all().order_by('-create_at')
    track = Track.objects.all().order_by('-create_at')
    category = Category.objects.all().order_by('-create_at')[:3]
    categorys = Category.objects.all().order_by('-create_at')
    blog = Blog.objects.all().order_by('-create_at')
    product = Product.objects.all().order_by('-create_at')
    payment = Payment.objects.all().order_by('-create_at')
    now = timezone.now()
    config = Config.objects.get(active = 1)
    date = Date.objects.get(active = 1)
    template = 'app/logins.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('app.logins'))
            else:
                # Redireccionar informando que la cuenta esta inactiva
                # Lo dejo como ejercicio al lector :)
                pass
        message = 'Datos de ingreso incorrectos. Intente de nuevo'
    return render_to_response(template,locals(),context_instance=RequestContext(request))

def signup_view(request):
    # Si el usuario esta ya logueado, lo redireccionamos a index_view
    if request.user.is_authenticated():
        return redirect(reverse('app.login'))
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(signup_view, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        return context
    if request.method == 'POST':
        # Si el method es post, obtenemos los datos del formulario
        form = signup_form(request.POST, request.FILES)
        # Comprobamos si el formulario es valido
        if form.is_valid():
            # En caso de ser valido, obtenemos los datos del formulario.
            cleaned_data = form.cleaned_data
            username = cleaned_data.get('username')
            password = cleaned_data.get('password')
            password2 = cleaned_data.get('password2')
            nickname = cleaned_data.get('nickname')
            phone = cleaned_data.get('phone')
            # E instanciamos un objeto User, con el username y password
            user_model = User.objects.create_user(username=username, password=password)
            # Y guardamos el objeto, esto guardara los datos en la db.
            user_model.save()
            # Ahora, creamos un objeto UserProfile
            user_profile = UserProfile()
            # Al campo user le asignamos el objeto user_model
            user_profile.user = user_model
            user_profile.nickname = nickname
            user_profile.phone = phone
            user_profile.password2 = password2
            user_profile.save()
            # Ahora, redireccionamos a la pagina
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse('app.welcome'), {'nickname': nickname})
                else:
                    # Redireccionar informando que la cuenta esta inactiva
                    pass
                message = 'Usuario incorrecto'
                return render(request, 'app/signup.html', {'message': message})
    else:
        # Si el mthod es GET, instanciamos un objeto RegistroUserForm vacio
        form = signup_form()
    # Creamos el contexto
    context = {'form': form}
    context['userprofile'] = UserProfile.objects.all()
    context['categorys'] = Category.objects.all()
    context['config'] = Config.objects.get(active = 1)
    context['viewl'] = 1
    # Y mostramos los datos
    return render(request, 'app/signup.html', context)

@login_required
def welcome_view(request):
    track = Track.objects.all().order_by('-create_at')
    userprofile = UserProfile.objects.all().order_by('-create_at')
    template = 'app/welcome.html'
    category = Category.objects.all().order_by('-create_at')[:3]
    categorys = Category.objects.all().order_by('-create_at')
    product = Product.objects.all().order_by('-create_at')
    blog = Blog.objects.all().order_by('-create_at')
    date = Date.objects.get(active = 1)
    now = timezone.now()
    config = Config.objects.get(active = 1)
    title = Link.objects.all().order_by('-create_at')
    return render_to_response(template,locals(),context_instance=RequestContext(request))

def us_view(request):
    message = ''
    userprofile = UserProfile.objects.all().order_by('-create_at')
    track = Track.objects.all().order_by('-create_at')
    category = Category.objects.all().order_by('-create_at')[:3]
    categorys = Category.objects.all().order_by('-create_at')
    blog = Blog.objects.all().order_by('-create_at')
    now = timezone.now()
    config = Config.objects.get(active = 1)
    template = 'app/us.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('app.login'))
            else:
                # Redireccionar informando que la cuenta esta inactiva
                # Lo dejo como ejercicio al lector :)
                pass
        message = 'Datos de ingreso incorrectos. Intente de nuevo'
    return render_to_response(template,locals(),context_instance=RequestContext(request))
    template = 'app/us.html'

def logout_view(request):
    logout(request)
    messages.success(request, 'Ingresa para continuar')
    return redirect(reverse('app.login'))

@login_required
def uploadtrack_view(request):
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(uploadtrack_view, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        return context
    if request.method == 'POST':
        # Si el method es post, obtenemos los datos del formulario
        form = uploadtrack_form(request.POST, request.FILES)
        # Comprobamos si el formulario es valido
        if form.is_valid():
            # En caso de ser valido, obtenemos los datos del formulario.
            cleaned_data = form.cleaned_data
            title = cleaned_data.get('title')
            audio = cleaned_data.get('audio')
            # E instanciamos un objeto User, con el username y password
        #    user_model = User.objects.create_user(username=username, password=password)
            # Y guardamos el objeto, esto guardara los datos en la db.
        #    user_model.save()
            # Ahora, creamos un objeto UserProfile
            track = Track()
            # Al campo user le asignamos el objeto user_model
           #track user_profile.user = user_model
            track.title = title
            track.audio = audio
            track.user = request.user
            track.save()
            message = 'Audio upload success'
            return redirect(reverse('app.welcome'), {'message': message})
            # Ahora, redireccionamos a la pagina
            #user = authenticate(username=username, password=password)
            #if user is not None:
             #   if user.is_active:
              #      login(request, user)
               #     return redirect(reverse('app.welcome'), {'nickname': nickname})
                #else:
                    # Redireccionar informando que la cuenta esta inactiva
                 #   pass
                #message = 'Usuario incorrecto'
    else:
        # Si el mthod es GET, instanciamos un objeto RegistroUserForm vacio
        form = uploadtrack_form()
    # Creamos el contexto
    context = {'form': form}
    context['userprofile'] = UserProfile.objects.all()
    context['config'] = Config.objects.get(active = 1)
    # Y mostramos los datos
    return render(request, 'app/uploadtrack.html', context)

def track_view(request, slug):
    template = 'app/track.html'
    config = Config.objects.get(active = 1)
    track = Track.objects.get(slug = slug)
    return render_to_response(template,locals(),context_instance=RequestContext(request))

def userprofile_view(request, slug):    
    # Si el usuario esta ya logueado, lo redireccionamos a index_view
    message = ''
    userprofile = UserProfile.objects.get(slug = slug)
    userprofiles = UserProfile.objects.all().order_by('-create_at')
    track = Track.objects.all().order_by('-create_at')
    category = Category.objects.all().order_by('-create_at')[:3]
    categorys = Category.objects.all().order_by('-create_at')
    blog = Blog.objects.all().order_by('-create_at')
    now = timezone.now()
    config = Config.objects.get(active = 1)
    template = 'app/userprofile.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('app.login'))
            else:
                # Redireccionar informando que la cuenta esta inactiva
                # Lo dejo como ejercicio al lector :)
                pass
        message = 'Datos de ingreso incorrectos. Intente de nuevo'
    return render_to_response(template,locals(),context_instance=RequestContext(request))

@login_required
def updateavatar_view(request, slug):
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context['userprofile'] = UserProfile.objects.get(slug=slug)
        context = super(updateavatar_view, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        return context
    if request.method == 'POST':
        # Si el method es post, obtenemos los datos del formulario
        form = updateavatar_form(request.POST, request.FILES)
        # Comprobamos si el formulario es valido
        if form.is_valid():
            # En caso de ser valido, obtenemos los datos del formulario.
            cleaned_data = form.cleaned_data
            avatar = cleaned_data.get('avatar')
            request.user.userprofile.avatar = avatar
            request.user.userprofile.save()
            message = 'Foto actualizada correctamente'
            return redirect(reverse('app.welcome'), {'message': message})
    else:
        # Si el mthod es GET, instanciamos un objeto RegistroUserForm vacio
        form = updateavatar_form()
    # Creamos el contexto
    context = {'form': form}
    context['config'] = Config.objects.get(active = 1)
    context['userprofile'] = UserProfile.objects.get(slug=slug)
    # Y mostramos los datos
    return render(request, 'app/updateavatar.html', context)
    
@login_required
def updatenickname_view(request, slug):
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context['userprofile'] = UserProfile.objects.get(slug=slug)
        context = super(updatenickname_view, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        return context
    if request.method == 'POST':
        # Si el method es post, obtenemos los datos del formulario
        form = updatenickname_form(request.POST)
        # Comprobamos si el formulario es valido
        if form.is_valid():
            # En caso de ser valido, obtenemos los datos del formulario.
            cleaned_data = form.cleaned_data
            nickname = cleaned_data.get('nickname')
            request.user.userprofile.nickname = nickname
            request.user.userprofile.save()
            message = 'Nombre de perfil actualizado correctamente'
            return redirect(reverse('app.welcome'), {'message': message})
    else:
        # Si el mthod es GET, instanciamos un objeto RegistroUserForm vacio
        form = updatenickname_form()
    # Creamos el contexto
    context = {'form': form}
    context['config'] = Config.objects.get(active = 1)
    context['userprofile'] = UserProfile.objects.get(slug=slug)
    # Y mostramos los datos
    return render(request, 'app/updatenickname.html', context)

#API REST

def response_mimetype(request):
    return 'application/json'

#data = serializers.serialize("json", SomeModel.objects.all())

class JSONResponse(HttpResponse):
    def __init__(self, obj='', json_opts=None, mimetype='application/json', *args, **kwargs):
        json_opts = json_opts if isinstance(json_opts, dict) else {}
        content =  json.dumps(obj, **json_opts) if isinstance(obj, dict) or isinstance(obj, list) else serializers.serialize("json",obj)
        super(JSONResponse, self).__init__(content, mimetype, *args, **kwargs)

class JSONListView(ListView):
    def get_queryset(self,*args,**kwargs):
        q = super(JSONListView,self).get_queryset(*args,**kwargs)
        if 'date' in self.request.GET:
                d = datetime.datetime.strptime(self.request.GET['date'],"%d-%m-%Y").date()
                q = q.filter(modified__gte=d)
        return q
    def render_to_response(self, context, **response_kwargs):
        response = JSONResponse(self.get_queryset(), mimetype=response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response
    def serialize(self,o):
        return str(o)

class TracksApi(JSONListView):
    model = Track

def device(request):
    if 'gcmid' in request.GET:
        o = GCMDevice.objects.create(registration_id=request.GET['gcmid'])
        if 'deviceid' in request.GET:
            o.device_id = request.GET['deviceid']
        o.save()
        return HttpResponse("True")
    return HttpResponse("False")

def categories_view(request):
    # Si el usuario esta ya logueado, lo redireccionamos a index_view
    message = ''
    userprofile = UserProfile.objects.all().order_by('-create_at')
    track = Track.objects.all().order_by('-create_at')
    category = Category.objects.all().order_by('-create_at')
    categorys = Category.objects.all().order_by('-create_at')
    blog = Blog.objects.all().order_by('-create_at')
    now = timezone.now()
    config = Config.objects.get(active = 1)
    template = 'app/categories.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('app.login'))
            else:
                # Redireccionar informando que la cuenta esta inactiva
                # Lo dejo como ejercicio al lector :)
                pass
        message = 'Datos de ingreso incorrectos. Intente de nuevo'
    return render_to_response(template,locals(),context_instance=RequestContext(request))

def category_view(request, slug):
    # Si el usuario esta ya logueado, lo redireccionamos a index_view
    message = 'category'
    userprofile = UserProfile.objects.all().order_by('-create_at')
    track = Track.objects.all().order_by('-create_at')
    category = Category.objects.all().order_by('-create_at')
    categorys = Category.objects.all().order_by('-create_at')
    blog = Blog.objects.all().order_by('-create_at')
    acategory = Category.objects.get(slug = slug)
    now = timezone.now()
    config = Config.objects.get(active = 1)
    template = 'app/category.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('app.login'))
            else:
                # Redireccionar informando que la cuenta esta inactiva
                # Lo dejo como ejercicio al lector :)
                pass
        message = 'Datos de ingreso incorrectos. Intente de nuevo'
    return render_to_response(template,locals(),context_instance=RequestContext(request))
    
def blog_view(request, slug):
    # Si el usuario esta ya logueado, lo redireccionamos a index_view
    message = ''
    userprofile = UserProfile.objects.all().order_by('-create_at')
    track = Track.objects.all().order_by('-create_at')
    category = Category.objects.all().order_by('-create_at')
    categorys = Category.objects.all().order_by('-create_at')
    blog = Blog.objects.all().order_by('-create_at')
    ablog = Blog.objects.get(slug = slug)
    now = timezone.now()
    config = Config.objects.get(active = 1)
    template = 'app/blog.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('app.login'))
            else:
                # Redireccionar informando que la cuenta esta inactiva
                # Lo dejo como ejercicio al lector :)
                pass
        message = 'Datos de ingreso incorrectos. Intente de nuevo'
    return render_to_response(template,locals(),context_instance=RequestContext(request))
    
# SERIE DE FUNCIONES ASINCRONAS <_
@login_required
def updatecolora_view(request, slug):
    userprofile = UserProfile.objects.get(slug = slug)
    template = 'app/welcome.html'
    color = '#512218'
    request.user.userprofile.color = color
    request.user.userprofile.save()
    message = 'Color actualizado correctamente'
    return redirect(reverse('app.welcome'), {'message': message})
@login_required
def updatecolorb_view(request, slug):
    userprofile = UserProfile.objects.get(slug = slug)
    template = 'app/welcome.html'
    color = '#077486'
    request.user.userprofile.color = color
    request.user.userprofile.save()
    message = 'Color actualizado correctamente'
    return redirect(reverse('app.welcome'), {'message': message})
@login_required
def updatecolorc_view(request, slug):
    userprofile = UserProfile.objects.get(slug = slug)
    template = 'app/welcome.html'
    color = '#777619'
    request.user.userprofile.color = color
    request.user.userprofile.save()
    message = 'Color actualizado correctamente'
    return redirect(reverse('app.welcome'), {'message': message})
@login_required
def updatecolord_view(request, slug):
    userprofile = UserProfile.objects.get(slug = slug)
    template = 'app/welcome.html'
    color = '#8d9091'
    request.user.userprofile.color = color
    request.user.userprofile.save()
    message = 'Color actualizado correctamente'
    return redirect(reverse('app.welcome'), {'message': message})
@login_required
def updatecolore_view(request, slug):
    userprofile = UserProfile.objects.get(slug = slug)
    template = 'app/welcome.html'
    color = '#84587b'
    request.user.userprofile.color = color
    request.user.userprofile.save()
    message = 'Color actualizado correctamente'
    return redirect(reverse('app.welcome'), {'message': message})
@login_required
def updatecolorf_view(request, slug):
    userprofile = UserProfile.objects.get(slug = slug)
    template = 'app/welcome.html'
    color = '#000'
    request.user.userprofile.color = color
    request.user.userprofile.save()
    message = 'Color actualizado correctamente'
    return redirect(reverse('app.welcome'), {'message': message})
@login_required
def updatecolorg_view(request, slug):
    userprofile = UserProfile.objects.get(slug = slug)
    template = 'app/welcome.html'
    color = '#a62517'
    request.user.userprofile.color = color
    request.user.userprofile.save()
    message = 'Color actualizado correctamente'
    return redirect(reverse('app.welcome'), {'message': message})
@login_required
def updatecolorh_view(request, slug):
    userprofile = UserProfile.objects.get(slug = slug)
    template = 'app/welcome.html'
    color = '#3f8e5e'
    request.user.userprofile.color = color
    request.user.userprofile.save()
    message = 'Color actualizado correctamente'
    return redirect(reverse('app.welcome'), {'message': message})
@login_required
def updatecolori_view(request, slug):
    userprofile = UserProfile.objects.get(slug = slug)
    template = 'app/welcome.html'
    color = '#4d5b93'
    request.user.userprofile.color = color
    request.user.userprofile.save()
    message = 'Color actualizado correctamente'
    return redirect(reverse('app.welcome'), {'message': message})
@login_required
def updatecolorj_view(request, slug):
    userprofile = UserProfile.objects.get(slug = slug)
    template = 'app/welcome.html'
    color = '#ff6c00'
    request.user.userprofile.color = color
    request.user.userprofile.save()
    message = 'Color actualizado correctamente'
    return redirect(reverse('app.welcome'), {'message': message})
@login_required
def updatecolork_view(request, slug):
    userprofile = UserProfile.objects.get(slug = slug)
    template = 'app/welcome.html'
    color = '#7d6222'
    request.user.userprofile.color = color
    request.user.userprofile.save()
    message = 'Color actualizado correctamente'
    return redirect(reverse('app.welcome'), {'message': message})
@login_required
def updatecolorl_view(request, slug):
    userprofile = UserProfile.objects.get(slug = slug)
    template = 'app/welcome.html'
    color = '#332607'
    request.user.userprofile.color = color
    request.user.userprofile.save()
    message = 'Color actualizado correctamente'
    return redirect(reverse('app.welcome'), {'message': message})

def tasks_view(request):
    message = ''
    userprofile = UserProfile.objects.all().order_by('-create_at')
    track = Track.objects.all().order_by('-create_at')
    category = Category.objects.all().order_by('-create_at')[:3]
    categorys = Category.objects.all().order_by('-create_at')
    blog = Blog.objects.all().order_by('-create_at')
    task = Task.objects.all().order_by('-create_at')
    now = timezone.now()
    config = Config.objects.get(active = 1)
    template = 'app/tasks.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('app.login'))
            else:
                # Redireccionar informando que la cuenta esta inactiva
                # Lo dejo como ejercicio al lector :)
                pass
        message = 'Datos de ingreso incorrectos. Intente de nuevo'
    return render_to_response(template,locals(),context_instance=RequestContext(request))

def companies_view(request):    
    # Si el usuario esta ya logueado, lo redireccionamos a index_view
    message = ''
    userprofiles = UserProfile.objects.all().order_by('-create_at')
    track = Track.objects.all().order_by('-create_at')
    category = Category.objects.all().order_by('-create_at')[:3]
    categorys = Category.objects.all().order_by('-create_at')
    blog = Blog.objects.all().order_by('-create_at')
    company = Company.objects.all().order_by('create_at')
    now = timezone.now()
    config = Config.objects.get(active = 1)
    template = 'app/companies.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('app.login'))
            else:
                # Redireccionar informando que la cuenta esta inactiva
                # Lo dejo como ejercicio al lector :)
                pass
        message = 'Datos de ingreso incorrectos. Intente de nuevo'
    return render_to_response(template,locals(),context_instance=RequestContext(request))
    
def dates_view(request):    
    # Si el usuario esta ya logueado, lo redireccionamos a index_view
    message = ''
    userprofiles = UserProfile.objects.all().order_by('-create_at')
    track = Track.objects.all().order_by('-create_at')
    category = Category.objects.all().order_by('-create_at')[:3]
    categorys = Category.objects.all().order_by('-create_at')
    blog = Blog.objects.all().order_by('-create_at')
    company = Company.objects.all().order_by('create_at')
    date = Date.objects.all().order_by('-create_at')
    now = timezone.now()
    config = Config.objects.get(active = 1)
    template = 'app/dates.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('app.login'))
            else:
                # Redireccionar informando que la cuenta esta inactiva
                # Lo dejo como ejercicio al lector :)
                pass
        message = 'Datos de ingreso incorrectos. Intente de nuevo'
    return render_to_response(template,locals(),context_instance=RequestContext(request))

def products_view(request):    
    # Si el usuario esta ya logueado, lo redireccionamos a index_view
    message = ''
    userprofiles = UserProfile.objects.all().order_by('-create_at')
    track = Track.objects.all().order_by('-create_at')
    category = Category.objects.all().order_by('-create_at')[:3]
    categorys = Category.objects.all().order_by('-create_at')
    blog = Blog.objects.all().order_by('-create_at')
    company = Company.objects.all().order_by('create_at')
    date = Date.objects.all().order_by('-create_at')
    product = Product.objects.all().order_by('-create_at')
    now = timezone.now()
    config = Config.objects.get(active = 1)
    template = 'app/products.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('app.login'))
            else:
                # Redireccionar informando que la cuenta esta inactiva
                # Lo dejo como ejercicio al lector :)
                pass
        message = 'Datos de ingreso incorrectos. Intente de nuevo'
    return render_to_response(template,locals(),context_instance=RequestContext(request))

def payments_view(request):    
    # Si el usuario esta ya logueado, lo redireccionamos a index_view
    message = ''
    userprofiles = UserProfile.objects.all().order_by('-create_at')
    track = Track.objects.all().order_by('-create_at')
    category = Category.objects.all().order_by('-create_at')[:3]
    categorys = Category.objects.all().order_by('-create_at')
    blog = Blog.objects.all().order_by('-create_at')
    company = Company.objects.all().order_by('create_at')
    date = Date.objects.all().order_by('-create_at')
    product = Product.objects.all().order_by('-create_at')
    payment = Payment.objects.all().order_by('-create_at')
    now = timezone.now()
    config = Config.objects.get(active = 1)
    template = 'app/payments.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('app.login'))
            else:
                # Redireccionar informando que la cuenta esta inactiva
                # Lo dejo como ejercicio al lector :)
                pass
        message = 'Datos de ingreso incorrectos. Intente de nuevo'
    return render_to_response(template,locals(),context_instance=RequestContext(request))
    
def payment_view(request, slug):    
    # Si el usuario esta ya logueado, lo redireccionamos a index_view
    payment = Payment.objects.get(slug = slug)
    message = ''
    userprofiles = UserProfile.objects.all().order_by('-create_at')
    track = Track.objects.all().order_by('-create_at')
    category = Category.objects.all().order_by('-create_at')[:3]
    categorys = Category.objects.all().order_by('-create_at')
    blog = Blog.objects.all().order_by('-create_at')
    company = Company.objects.all().order_by('create_at')
    date = Date.objects.all().order_by('-create_at')
    product = Product.objects.all().order_by('-create_at')
    now = timezone.now()
    config = Config.objects.get(active = 1)
    template = 'app/payment.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('app.login'))
            else:
                # Redireccionar informando que la cuenta esta inactiva
                # Lo dejo como ejercicio al lector :)
                pass
        message = 'Datos de ingreso incorrectos. Intente de nuevo'
    return render_to_response(template,locals(),context_instance=RequestContext(request))


@login_required
def cart_view(request):
    template = 'app/cart.html'
    config = Config.objects.get(active = 1)
    cart = Cart.objects.all().order_by('-create_at')
    return render_to_response(template,locals(),context_instance=RequestContext(request))

@login_required
def addcart_view(request, slug):
    product = Product.objects.get(slug = slug)
    template = 'app/cart.html'
    cart = Cart()
    cart.product = product
    cart.price = product.price
    cart.cant = 1
    cart.owner = request.user.userprofile
    cart.save()
    message = 'Producto agregado a su lista de compras'
    return redirect(reverse('app.cart'), {'message': message})
    
@login_required
def deletecart_view(request, slug):
    cart = Cart.objects.get(slug = slug)
    cart.delete()
    message = 'Producto eliminado'
    return redirect(reverse('app.cart'), {'message': message})

@login_required
def addbuyment_view(request):
    template = 'app/buyment.html'
    config = Config.objects.get(active = 1)
    payment = Payment.objects.all().order_by('-create_at')
    buyments = Buyment.objects.all().order_by('-create_at')
    buyment = Buyment()
    buyment.buyment = request.user.userprofile
    buyment.save()
    message = 'Confirmar orden'
    return redirect(reverse('app.buyment'), {'message': message})

def confirmbuy_view(request):
    template = 'app/confirmbuy.html'
    message = 'Su orden se esta procesando.'
    return render_to_response(template,locals(),context_instance=RequestContext(request))

@login_required
def buyment_view(request):
    def get_context_data(self, **kwargs):
        context = super(buyment_view, self).get_context_data(**kwargs)
        return context
    if request.method == 'POST':
        form = payment_form(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            title = cleaned_data.get('title')
            picture = cleaned_data.get('picture')
            description = cleaned_data.get('description')
            amount = cleaned_data.get('amount')
            name = cleaned_data.get('name')
            tlf = cleaned_data.get('tlf')
            address = cleaned_data.get('address')
            boucher = Boucher()
            boucher.title = title
            boucher.amount = amount
            boucher.tlf = tlf
            boucher.name = name
            boucher.address = address
            boucher.picture = picture
            boucher.description = description
            boucher.owner = request.user.userprofile
            boucher.save()
            message = 'Confirmacion enviada'
            return redirect(reverse('app.confirmbuy'), {'message': message})
    else:
        form = payment_form()
    context = {'form': form}
    context['buyments'] = Buyment.objects.all().order_by('-create_at')[:1]
    context['payment'] = Payment.objects.all().order_by('-create_at')
    context['config'] = Config.objects.get(active = 1)
    return render(request, 'app/buyment.html', context)
    
def paymentc_view(request):
    def get_context_data(self, **kwargs):
        context = super(paymentc_view, self).get_context_data(**kwargs)
        return context
    if request.method == 'POST':
        form = paymentc_form(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            title = cleaned_data.get('title')
            picture = cleaned_data.get('picture')
            description = cleaned_data.get('description')
            amount = cleaned_data.get('amount')
            name = cleaned_data.get('name')
            tlf = cleaned_data.get('tlf')
            address = cleaned_data.get('address')
            boucher = Boucher()
            boucher.title = title
            boucher.amount = amount
            boucher.tlf = tlf
            boucher.name = name
            boucher.address = address
            boucher.picture = picture
            boucher.description = description
            boucher.save()
            message = 'Confirmacion enviada'
            return redirect(reverse('app.confirmbuy'), {'message': message})
    else:
        form = payment_form()
    context = {'form': form}
    context['buyments'] = Buyment.objects.all().order_by('-create_at')[:1]
    context['payment'] = Payment.objects.all().order_by('-create_at')
    context['config'] = Config.objects.get(active = 1)
    return render(request, 'app/buyment.html', context)
    
def createblog_view(request):
    def get_context_data(self, **kwargs):
        context = super(createblog_view, self).get_context_data(**kwargs)
        return context
    if request.method == 'POST':
        form = createblog_form(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            title = cleaned_data.get('title')
            picture = cleaned_data.get('picture')
            description = cleaned_data.get('description')
            category = cleaned_data.get('category')
            blog = Blog()
            blog.title = title
            blog.category = category
            blog.picture = picture
            blog.description = description
            blog.save()
            message = 'Blog publicado'
            return redirect(reverse('app.blogs'), {'message': message})
    else:
        form = createblog_form()
    context = {'form': form}
    context['buyments'] = Buyment.objects.all().order_by('-create_at')[:1]
    context['payment'] = Payment.objects.all().order_by('-create_at')
    context['category'] = Category.objects.all().order_by('-create_at')
    context['config'] = Config.objects.get(active = 1)
    return render(request, 'app/createblog.html', context)
    
def blogs_view(request):    
    # Si el usuario esta ya logueado, lo redireccionamos a index_view
    message = ''
    userprofiles = UserProfile.objects.all().order_by('-create_at')
    track = Track.objects.all().order_by('-create_at')
    category = Category.objects.all().order_by('-create_at')[:3]
    categorys = Category.objects.all().order_by('-create_at')
    blog = Blog.objects.all().order_by('-create_at')
    company = Company.objects.all().order_by('create_at')
    date = Date.objects.all().order_by('-create_at')
    product = Product.objects.all().order_by('-create_at')
    payment = Payment.objects.all().order_by('-create_at')
    now = timezone.now()
    config = Config.objects.get(active = 1)
    template = 'app/blogs.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('app.login'))
            else:
                # Redireccionar informando que la cuenta esta inactiva
                # Lo dejo como ejercicio al lector :)
                pass
        message = 'Datos de ingreso incorrectos. Intente de nuevo'
    return render_to_response(template,locals(),context_instance=RequestContext(request))
    
    
def search(request):
    userprofile = UserProfile.objects.all().order_by('-create_at')
    track = Track.objects.all().order_by('-create_at')
    category = Category.objects.all().order_by('-create_at')
    blog = Blog.objects.all().order_by('-create_at')
    product = Product.objects.all().order_by('-create_at')
    company = Product.objects.all().order_by('-create_at')
    date = Date.objects.all().order_by('-create_at')
    payment = Payment.objects.all().order_by('-create_at')
    boucher = Boucher.objects.all().order_by('-create_at')
    cart = Cart.objects.all().order_by('-create_at')
    buyment = Buyment.objects.all().order_by('-create_at')
    wallet = Wallet.objects.all().order_by('-create_at')
    link = Link.objects.all().order_by('-create_at')
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(name__icontains=query) | Q(userprofile__nickname__icontains=query) 
            | Q(track__title__icontains=query) | Q(category__title__icontains=query) | Q(category__description__icontains=query) | Q(blog__title__icontains=query) | Q(blog__description__icontains=query) | Q(product__title__icontains=query) | Q(product__description__icontains=query) | Q(company__title__icontains=query) | Q(company__description__icontains=query) | Q(date__title__icontains=query) | Q(date__description__icontains=query)
        )
        results = UserProfile.objects.filter(qset).order_by('nickname').distinct()
    else:
        results = []
    return render_to_response("app/search.html", {
        "results": results,
        "query": query,
        "userprofile": userprofile,
        "track": track,
        "category": category,
        "blog": blog,
        "product": product,
        "company": company,
        "date": date,
        "payment": payment,
        "boucher": boucher,
        "buyment": buyment,
        "wallet": wallet,
        "link": link,
    })