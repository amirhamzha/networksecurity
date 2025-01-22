from setuptools import find_packages,setup

from typing import List

def get_requirements()->List[str]:
    """ this function will return list of requirements
    """

    requirement_lst:list[str]=[]

    try:
        with open('requirements.txt','r') as file:
            #read lines from the file
            lines=file.readlines()
            ## process each line
            for line in lines:
                requirement=line.strip()
                ## ignore empty lines and -e .

                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)


    except FileNotFoundError: 

        print("requirments.txt not found")    


    return requirement_lst               


setup(name="NetworkSecurity",
    version="0.0.1",
    author="krish Naik",
    author_email="Amirhamzha.1997@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)

    