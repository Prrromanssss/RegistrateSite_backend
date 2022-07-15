from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrateForm, LoginForm
from .models import Registrate
import json


def index(request):
    return render(request, 'registrate/index.html')


def register(request):
    if request.method == 'POST':
        form = RegistrateForm(request.POST)
        if form.is_valid():
            with open('registrate/data.json', encoding='utf-8') as file:
                try:
                    data = json.loads(file.read())
                except json.decoder.JSONDecodeError:
                    data = []
                print(data)
            with open('registrate/data.json', 'w', encoding='utf-8') as file:
                flag = True
                for users in range(len(data)):
                    print(str(data[users].keys()) == f"dict_keys([{repr(form.cleaned_data['email'])}])")
                    if str(data[users].keys()) == f"dict_keys([{repr(form.cleaned_data['email'])}])":
                        form.cleaned_data.update({'id_name': RegistrateForm.id_name})
                        data[users] = {form.cleaned_data['email']: form.cleaned_data}
                        flag = False
                if flag:
                    form.cleaned_data.update({'id_name': RegistrateForm.id_name})
                    data.append({form.cleaned_data['email']: form.cleaned_data})
                RegistrateForm.id_name += 1
                json.dump(data, file, indent=4, ensure_ascii=False)
            print(form.cleaned_data)

    else:
        form = RegistrateForm()
    return render(request, 'registrate/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            with open('registrate/data.json') as file:
                try:
                    data = json.loads(file.read())
                except json.decoder.JSONDecodeError:
                    return render(request, 'registrate/bad_login.html')
                flag = False
                for users in range(len(data)):
                    if str(data[users].keys()) == f"dict_keys([{repr(form.cleaned_data['email'])}])":
                        print(data[users])
                        if form.cleaned_data['password'] == data[users][form.cleaned_data['email']]['password']:
                            return render(request, 'registrate/account.html', {'form': data[users][form.cleaned_data['email']]})
                        else:
                            flag = True
                if flag:
                    return render(request, 'registrate/bad_login.html')
    else:
        form = LoginForm()
    return render(request, 'registrate/login.html', {'form': form})
