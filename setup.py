from setuptools import find_packages,setup
from typing import List


hypen_e_dot ='-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[] # here we have created an empty list
    with open(file_path) as file_obj:
        requirements=file_obj.readlines() # here we have read the lines of the file
        requirements=[req.replace("\n","") for req in requirements] # here we have replaced the \n with empty string
        
        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)

        return requirements


setup(
    name = 'DiamondPricePrediction',
    version='0.0.1',
    author=['Gitesh Suresh Ratnaparkhi ',' Silki Nitin Ghoshikar'],
    author_email=["giteshratnaparkhi@gmail.com","silkighoshikar@gmail.com"],
    insatall_requires=get_requirements('requirements.txt'),
    packages=find_packages(),
)