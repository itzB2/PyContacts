import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='vcard',  
     version='0.1',
     scripts=['dokr'] ,
     author="Judah Beethoven",
     author_email="masterofcoding360@gmail.com",
     description="A VCF card generator",
     long_description=long_description,
   long_description_content_type="text/markdown",
    url="https://github.com/judah-b2/Vcard",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
