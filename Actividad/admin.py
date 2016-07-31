from django.contrib import admin
#from .models import Actividad
from .models import Acti
from .models import Usuario
from .models import Departamentos
from .models import HistorialDeVisitas
from .models import Sesion
#myModels=[]
# Register your models here.
admin.site.register(Acti)
admin.site.register(Usuario)
admin.site.register(Departamentos)
admin.site.register(HistorialDeVisitas)
admin.site.register(Sesion)