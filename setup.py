import os

from setuptools import find_packages, setup
from setuptools.command.develop import develop


class CustomDevelopCommand(develop):
    """Instal development dependencies"""

    def install_for_development(self):
        os.system("pip install '.[development]'")
        os.system("pre-commit install")


__version__ = "0.0.3"

requires = ["cryptography >= 37.0.2"]

extras = {
    "test": ["pytest >= 7.1.2"],
    "development": ["black >= 22.3.0", "isort >= 5.10.1", "pre-commit >= 2.19.0"],
}

with open("README.rst") as f:
    long_description = f.read()

setup(
    name="aes_pkcs5",
    version=__version__,
    description="Implementation of AES with CBC/ECB mode and padding scheme PKCS5",
    long_description=long_description,
    author="Laerte Pereira",
    author_email="hi@laerte.dev",
    url="https://github.com/Laerte/aes_pkcs5",
    packages=find_packages(include=["aes_pkcs5*"], exclude=["tests.*"]),
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    include_package_data=True,
    install_requires=requires,
    extras_require=extras,
    cmdclass={"develop": CustomDevelopCommand},
)
