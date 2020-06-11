from django.shortcuts import render
from imm.core.extension import Extension

extension = Extension(name="{{cookiecutter.package_name}}")


@extension.ready
def ready():
    extension.log.info("Extension {{cookiecutter.package_name}} is running")


@extension.view('/')
def index(request):
    return render(request, '{{cookiecutter.package_name}}/hello_world.html')
