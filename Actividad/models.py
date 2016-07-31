from django.db import models
from django.utils import timezone


class Acti(models.Model):
    organismo = models.CharField(max_length=50)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    documentacion = models.TextField()
    recompensa=models.IntegerField()
    identificacion=models.IntegerField(default=0)
    url=models.CharField(max_length=200,default="www.google.com")
    
    def getId(self):
        return self.identificacion
    def publish(self):
        self.save()

    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    curp = models.CharField(max_length=20, default=" ")
    password = models.CharField(max_length=20)
    monedas=models.PositiveIntegerField()
    correo=models.CharField(max_length=90)
    title=models.CharField(max_length=90, default='user1')
    def getCoins(self):
        return self.monedas
    def quitarPuntos(self,puntos):
        self.monedas=self.monedas-puntos
    def agregarPuntos(self, puntos):
        self.monedas=self.monedas+puntos
    def getPass(self):
        return self.password
    def publish(self):
        self.save()
    def __str__(self):
        return self.title
    
class Departamentos(models.Model):
    title=models.CharField(max_length=90, default='depto1')
    monedasMaximas=models.PositiveIntegerField(default=999)
    monedasDadas=models.PositiveIntegerField(default=0)

    def publish(self):
        self.save()
    def __str__(self):
        return self.title

    def saldoPorPagar(self, monedasTotales, costoTotal):
        costoPorMoneda=costoTotal/monedasTotales
        return self.monedasDadas*costoPorMoneda

class HistorialDeVisitas(models.Model):
    user=models.CharField(max_length=90, default='user1')
    evento=models.IntegerField(default=0)
    def publish(self):
        self.save()

class Sesion(models.Model):
    userTitle=models.CharField(max_length=90, default='user1')
    def getUser(self):
        return self.userTitle
    def publish(self):
        self.save()

class HistoriaPremios(models.Model):
    area=models.CharField(max_length=90, default='user1')
    concepto=models.CharField(max_length=400, default='user1')
    fecha=models.DateTimeField(default=timezone.now)
    usuario=models.CharField(max_length=90, default='user1')
    def publish(self):
        self.save()



