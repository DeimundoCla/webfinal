from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Posteo(models.Model):
    titulo = models.CharField(max_length=60)
    subtitulo = models.CharField(max_length=120)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    contenido = RichTextField(blank=True)
    imagen = models.ImageField(upload_to='images/')
    url = models.SlugField(max_length=264, unique=True)
   
    def __str__(self):
        return self.titulo + ' | ' + str(self.autor)

    def save(self, *args, **kwargs):
        self.url = slugify(self.titulo)
        super(Posteo, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("post", kwargs={"url": self.url})

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    telefono = models.CharField(max_length=50)
    mensaje = models.TextField(max_length=500)

    def __str__(self):
        return self.nombre + ' | ' + self.email