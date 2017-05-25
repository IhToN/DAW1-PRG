from distutils.core import setup
import py2exe

setup(
    name='Facturacion',
    version='1.0',
    packages=['', 'Objects', 'Collections', 'Controllers'],
    url='https://atalgaba.com',
    license='GNU GENERAL PUBLIC LICENSE',
    author='IhToN',
    author_email='atalgaba@gmail.com',
    description='Programa simple de facturación',
    console=['Facturacion.py']
)
