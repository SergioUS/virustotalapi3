from setuptools import setup, find_packages
import vtapi3

setup(
    name='vtapi3',
    version=vtapi3.__version__,
    author='Evgeny Drobotun',
    author_email='drobotun@xakep.ru',
    url='https://github.com/drobotun/virustotalapi3',
    zip_safe=False,
    license=vtapi3.__license__,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite='test_vt_3',
    packages=['vtapi3'],
    install_requires=['requests >= 2.22.0'])