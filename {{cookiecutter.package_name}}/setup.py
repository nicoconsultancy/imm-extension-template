from setuptools import setup, find_packages

requirements = open('requirements.txt').readlines()
readme = open('README').read()

setup(
    name="{{cookiecutter.package_name}}",
    version="{{cookiecutter.version}}",

    description='{{cookiecutter.project_name}}',
    long_description=readme,
    url='{{cookiecutter.support_website}}',
    author='{{cookiecutter.vendor_name}}',
    author_email='{{cookiecutter.support_email}}',

    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "imm_extension": [
            "{{cookiecutter.package_name}} = {{cookiecutter.package_name}}.extension.extension",
        ]
    },

    python_requires='>=3.8, <4',
    install_requires=[
        'imm',
        'imm.api',
    ] + requirements,

    zip_safe=False
)
