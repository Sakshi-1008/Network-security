from setuptools import find_packages,setup
from typing import List

def get_requrimenets()->List[str]:

    requirement_lst:List[str] = [] 
    try:
        with open('requirements.txt') as file:
            ##read lines ffom the file
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                ##ignore empty line and -e.
                if requirement and requirement != '-e .':
                   requirement_lst.append(requirement)
    
    except FileNotFoundError:
        print("requirement.txt not found")
 
    return requirement_lst

setup(
    name = "Network security",
    version = "0.0.1",
    author= "Sakshi Patel",
    author_email= "sakshipatel@gmail.com",
    packages = find_packages(),
    install_requires = get_requrimenets()

)
