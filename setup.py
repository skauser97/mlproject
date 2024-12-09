# responsible in creating my ml application as a pacage which can then be used in other projects
#and also deploy in py py
from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path: str)->List[str]:
    '''
    this func returns list of requirements
    '''
    requirements= []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements
    



setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'sadia',
    author_email= 'sadi.kar97@gmail.com',
    packages = find_packages(), # checks how many folders 
    #have __init__.py. will consider src as package and will try to build it
    install_requires = get_requirements('requirements.txt') #['pandas', 'numpy', 'seaborn']

)

#-e . triggers setup.py file in requirements.txt