from setuptools import setup, find_packages

setup(
    name='jper-oaipmh',
    version='1.0.2',
    packages=find_packages(),
    install_requires=[
        "esprit",
        "octopus",
        "Flask<3.0"
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
