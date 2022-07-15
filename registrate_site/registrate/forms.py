from django import forms


class RegistrateForm(forms.Form):
    id_name = 0
    name = forms.CharField(max_length=150,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    surname = forms.CharField(max_length=150,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField()
    email = forms.EmailField(max_length=246)
    password = forms.CharField(max_length=150)


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=246)
    password = forms.CharField(max_length=150)