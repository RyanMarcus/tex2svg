import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tex2svg",
    version="0.0.1",
    author="Ryan Marcus",
    author_email="ryan@ryanmarc.us",
    description="A script to convert LaTeX snippets to SVG",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RyanMarcus/tex2svg",
    packages=setuptools.find_packages(),
    scripts=["bin/tex2svg"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
)
