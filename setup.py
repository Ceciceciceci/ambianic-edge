import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ambianic-ivelin",
    version="0.0.1",
    author="Ivelin Ivanov",
    author_email="ivelin117@gmail.com",
    description="AI framework for home and business automation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://ambianic.ai",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache 2.0",
        "Operating System :: OS Independent",
    ],
)