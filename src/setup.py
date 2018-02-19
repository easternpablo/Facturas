__author__ = "a16pablovm"
__date__ = "$Feb 19, 2018 2:37:34 PM$"

from setuptools import setup, find_packages

setup (
       name='Factura',
       version='0.1',
       packages=find_packages(),

       # Declare your packages' dependencies here, for eg:
       install_requires=['foo>=3'],

       # Fill in these to make your Egg ready for upload to
       # PyPI
       author='a16pablovm',
       author_email='',

       summary='Just another Python package for the cheese shop',
       url='',
       license='',
       long_description='Long description of the package',

       # could also include long_description, download_url, classifiers, etc.

  
       )