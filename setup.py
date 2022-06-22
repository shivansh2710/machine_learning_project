from gettext import install
from xml.etree.ElementTree import VERSION
from setuptools import setup
from typing import List


#declaring variable for setup functions
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR = "shivansh sarathe"
DESCRIPTION = "this is first Machine Learning project"
#Packages is install during run time
PACKAGES = ["housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"

#this function is going to return list which have string value in it
def get_requirements_list()->List[str]:
    """
    Description : This function is going to retrun list of requirement mention in requirement.txt file

    return this function is going to return a list which contains name of libraries mentioned in requirement
    .txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_file.readline


 
setup(
    name= PROJECT_NAME,
    version  = VERSION,
    author = AUTHOR,
    description =  DESCRIPTION,
    packages = PACKAGES,
    install_requires = get_requirements_list() 
)

