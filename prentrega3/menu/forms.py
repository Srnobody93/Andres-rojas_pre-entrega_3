from django import forms

class usuarioForm(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField()
    age = forms.IntegerField()

class distribuidorForm(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField()
    company = forms.CharField(max_length=30)
    distributor_numbre = forms.IntegerField()

class productoForm(forms.Form):
    codigo = forms.IntegerField()