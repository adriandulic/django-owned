# -*- coding: utf-8 -*-
from setuptools import setup
import os

def packages():
    packages = []
    for path, dirs, files in os.walk("."):
        if '.svn' in dirs:
            dirs.remove('.svn')
        if '__init__.py' in files:
            packages.append(path.replace(os.sep, "."))
    return packages

setup(
    name='django-owned',
    version=__import__('owned').__version__,
    description='Model object ownership for Django',
    long_description=open('docs/overview.txt').read(),
    author='Adrian Dulić',
    author_email='adulic@gmail.com',
    url='http://github.com/adriandulic/django-owned',
    packages=packages(),
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
)
