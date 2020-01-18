import setuptools
from filepart import __version__

with open("README.md", "r") as f:
    long_description = f.read()

"""
requirements = []
with open('requirements.txt') as f:
  requirements = f.read().splitlines()
"""

setuptools.setup(
    name="filepart",
    version=__version__,
    author="UnknownPlayer78",
    author_email="info@tearlabs.xyz",
    description="Split files into separate parts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.2',
    scripts=['bin/filepart'],
    #install_requires=requirements,
    url="https://github.com/UnknownPlayer78/filepart",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
