from setuptools import setup

DESCRIPTION = "A Django email backend for Amazon Simple Email Service, backed by celery."

LONG_DESCRIPTION = open('README.rst').read()

CLASSIFIERS = [
    'Environment :: Web Environment',
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Framework :: Django',
]

setup(
    name='seacucumber-py3',
    version='1.5.2',
    packages=[
        'seacucumber',
        'seacucumber.management',
        'seacucumber.management.commands',
    ],
    author='Gregory Taylor',
    author_email='gtaylor@duointeractive.com',
    maintainer='Gordon Vu',
    maintainer_email='gordon.vu@gmail.com',
    url='https://github.com/gordon86/sea-cucumber',
    license='MIT',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    platforms=['any'],
    classifiers=CLASSIFIERS,
    install_requires=['boto>=2.25.0', 'celery'],
)
