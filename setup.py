import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-h5bp',
    version='0.3.3',
    packages=['django_h5bp'],
    include_package_data=True,
    license='MIT License',
    description='A simple HTML5 Boilerplate Django app that has some predefined template Blocks, useful to be extended in any application template.',
    long_description=README,
    url='https://github.com/arruda/django-h5bp',
    author='Felipe Arruda Pontes',
    author_email='contato@arruda.blog.br',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
