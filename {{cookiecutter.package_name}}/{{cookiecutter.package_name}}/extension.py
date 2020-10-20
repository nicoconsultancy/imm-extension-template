from django.shortcuts import render
from .const import extension

@extension.view(path='/')
def index(request):
    return render(request, '{{cookiecutter.package_name}}/index.html')
