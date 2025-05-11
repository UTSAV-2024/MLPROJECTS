from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = "-e ."
def get_requirements(file_path: str) -> List['str']:
    """
    This function reads a requirements file and returns a list of required packages.
    
    Args:
    file_path (str): The path to the requirements file.
    
    Returns:
    list: A list of required packages.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        return requirements
setup(
    name="ML-Project",
    version="0.0.1",
    author="UTSAV",
    author_email="utsavkumar1283@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
    ) 
# This is a setup script for a Python package named "ML-Project".


