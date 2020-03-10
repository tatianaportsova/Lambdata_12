# setup.py

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="tt.sova-lambdata-12", # Replace with your own username
    version="0.0.1",
    author="Tatiana Portsova",
    author_email="tt.sova@gmail.com",
    description="For example purposes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tatianaportsova/Lambdata_12",
    packages=find_packages()  # ["my_lambdata"]
)
