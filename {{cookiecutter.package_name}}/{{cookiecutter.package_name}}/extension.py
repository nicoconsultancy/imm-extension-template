from django.shortcuts import render
from imm.core.extension import Extension

extension = Extension()


@extension.view('/')
def index(request):
    return render(request, '{{cookiecutter.package_name}}/hello_world.html')
