from os import system

from setuptools import setup
from setuptools.command.develop import develop


class CustomDevelopCommand(develop):
    """Instal development dependencies"""

    def install_for_development(self):
        system("pip install -r requirements-dev.txt")
        system("pre-commit install")


setup(cmdclass={"develop": CustomDevelopCommand})
