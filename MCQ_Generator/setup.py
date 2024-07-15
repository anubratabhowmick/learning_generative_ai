"""
A setup script for the 'mcqgenerator' package.

This script uses setuptools to package the 'mcqgenerator' project. It includes
metadata about the project, such as the name, version, author, and dependencies.

Dependencies:
    - openai
    - langchain
    - streamlit
    - python-dotenv
    - PyPDF2

The packages are automatically discovered using find_packages().

Attributes:
    name (str): The name of the package.
    version (str): The current version of the package.
    author (str): The name of the author.
    install_requires (list): A list of required dependencies.
    packages (list): A list of all Python import packages that should be included in the distribution package.
"""

from setuptools import find_packages, setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='Anubrata Bhowmick',
    install_requires = ['openai', 'langchain', 'streamlit', 'python-dotenv', 'PyPDF2'],
    packages=find_packages()
)
