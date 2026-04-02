from setuptools import setup, find_packages
from typing import List

def get_requirements(file_name: str) -> List[str]:
    requirements = []
    with open(file_name) as requirements_file:
        requirements = requirements_file.readlines()
        requirements=[req.replace("\n", "") for req in requirements]
        if '-e .' in requirements:
            requirements.remove('-e .')

    return requirements


setup(
    name='practice_ml',
    version='0.0.1',
    author='mohit',
    author_email='inbox.mohittiwari@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)