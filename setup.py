from setuptools import setup, find_packages

setup(
    name='jper-oaipmh',
    version='1.0.0-p3',
    packages=find_packages(),
    install_requires=[
        "esprit",
        "octopus",
        "Flask==1.1.2"
    ],
    url='http://cottagelabs.com/',
    author='Cottage Labs',
    author_email='us@cottagelabs.com',
    description='OAI-PMH endpoint for JPER',
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
