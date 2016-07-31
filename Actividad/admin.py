from django.contrib import admin
#from .models import Actividad
from .models import Acti
from .models import Usuario
from .models import Departamentos
#myModels=[]
# Register your models here.
admin.site.register(Acti)

admin.site.register(Usuario)
admin.site.register(Departamentos)