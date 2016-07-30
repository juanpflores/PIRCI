from django.db import models
 


class Actividad(models.Model):
    organismo = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    #imagen ..... https://docs.djangoproject.com/es/1.9/ref/models/fields/
    documentacion = models.TextField()
    recompensa=models.IntegerField()
    #boton=models.BooleanField()


    def publish(self):
        self.save()

    def __str__(self):
        return self.titulo