  from django import forms

    from .models import Usuario

    class registraUsuario(forms.ModelForm):

        class Meta:
            model = Usuario
            fields = ('curp', 'mail','userN','pass')