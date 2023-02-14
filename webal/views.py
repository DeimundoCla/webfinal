from django.shortcuts import render, HttpResponse, redirect
from django.template import loader
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import ListView, DetailView
from .models import Posteo
from .forms import ContactoForm

class Vistaposteo(DetailView):
    model = Posteo
    template_name = 'post.html'
    slug_field = 'url'
    slug_url_kwarg = 'url'

class Home(ListView):
    model = Posteo
    template_name = 'index.html'
    ordering = ['-fecha_publicacion']

def contacto(request):
    form = ContactoForm()
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']
            send_mail(
                'Mensaje de ' + nombre,
                mensaje,
                email,
                ['deimundocla@gmail.com'])
        return redirect( "index.html")
    else:
        form = ContactoForm()
    
    
    return render(request, "contacto.html", { 'form': form})

def error404(request):
    template = loader.get_template("404.html")
    documento = template.render()
    return HttpResponse(documento)

def about(request):
    template = loader.get_template("about.html")
    documento = template.render()
    return HttpResponse(documento)

def remodelaciones(request):
    template = loader.get_template("remodelaciones.html")
    documento = template.render()
    return HttpResponse(documento)

def servicios(request):
    template = loader.get_template("servicios.html")
    documento = template.render()
    return HttpResponse(documento)

class Remodelaciones(ListView):
    model = Posteo
    template_name = 'remodelaciones.html'
    ordering = ['-fecha_publicacion']