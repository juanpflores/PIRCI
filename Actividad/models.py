from django.db import models
 


class Acti(models.Model):
    organismo = models.CharField(max_length=50)
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

class Usuario(models.Model):
    curp = models.CharField(max_length=20)
    userName = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    monedas=models.IntegerField()
    title=models.CharField(max_length=20, default='blah')

   
    def publish(self):
        self.save()

    def __str__(self):
        return self.title