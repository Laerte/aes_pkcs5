from os import system

from setuptools import find_packages, setup
from setuptools.command.develop import develop

from aes_pkcs5 import __version__


class CustomDevelopCommand(develop):
    """Instal development dependencies"""

    def install_for_development(self):
        system("pip install -r requirements-dev.txt")
        system("pre-commit install")


requires = ["cryptography >= 38.0.1"]

extras = {}

with open("README.rst") as f:
    long_description = f.read()

setup(
    name="aes_pkcs5",
    version=__version__,
    description="Implementation of AES with CBC/ECB mode and padding scheme PKCS5",
    long_description=long_description,
    author="Laerte Pereira",
    author_email="hi@laerte.dev",
    license="BSD",
    url="https://github.com/Laerte/aes_pkcs5",
    packages=find_packages(include=["aes_pkcs5*"], exclude=["tests.*"]),
    classifiers=[
        "Intended Audience :: Developers",
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    include_package_data=True,
    install_requires=requires,
    extras_require=extras,
    cmdclass={"develop": CustomDevelopCommand},
)
