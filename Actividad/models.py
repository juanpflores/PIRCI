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
    curp = models.CharField(max_length=20, default=" ")
    password = models.CharField(max_length=20)
    monedas=models.PositiveIntegerField()
    correo=models.CharField(max_length=90)
    title=models.CharField(max_length=90, default='user1')

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

    def __saldoPorPagar__(self, monedasTotales, costoTotal):
        costoPorMoneda=costoTotal/monedasTotales
        return self.monedasDadas*costoPorMoneda
