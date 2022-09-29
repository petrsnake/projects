from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

try:
    with open("README.md", "r") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = "README.md not found"

try:
    with open('requirements.txt') as fh:
        required = fh.read().splitlines()
except FileNotFoundError:
    required = []
_version_ = "0.1"

setup(
    name="ReadFile",  # Required
    version=_version_,
    description="Primitive copy of head command", 
    long_description=long_description,
    url="https://github.com/petrsnake/projects", 
    author="Petr Žůček, Jan Harenčák",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    packages=find_packages(), 
    python_requires=">=3.7, <4",
    install_requires=required,
    entry_points={  # Optional
        "console_scripts": [
            "readfile=read_file.main:main",
        ],
    }
)