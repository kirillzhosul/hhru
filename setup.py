"""
HH.ru API library for Python.
Setup tools script.
"""

import os
from typing import Any, Dict

from setuptools import find_packages, setup

# Read and pass all data from version file (module.)
version_file: Dict[str, Any] = {}
with open(
    os.path.join(os.path.abspath(os.path.dirname(__file__)), "hhru", "__version__.py"),
    "r",
    encoding="utf-8",
) as f:
    exec(f.read(), version_file)

# Read whole readme file.
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

classifiers = [
    "Development Status :: 3 - Alpha",
    "Environment :: Web Environment",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Topic :: Software Development :: Libraries :: Python Modules",
]
project_urls = {
    "Documentation": "https://github.com/kirillzhosul/hhru",
    "Source": "https://github.com/kirillzhosul/hhru",
}
setup(
    name=version_file["__title__"],
    version=version_file["__version__"],
    description=version_file["__description__"],
    long_description=readme,
    long_description_content_type="text/markdown",
    author=version_file["__author__"],
    author_email=version_file["__author_email__"],
    url=version_file["__url__"],
    packages=find_packages(),
    package_data={"": ["LICENSE"], "hhru": ["py.typed"]},
    keywords=["hhru", "hh.ru", "hh api", "headhunter"],
    package_dir={"hhru": "hhru"},
    include_package_data=True,
    license=version_file["__license__"],
    python_requires=">=3.10",
    install_requires=["requests^2.28.1"],
    classifiers=classifiers,
    project_urls=project_urls,
    zip_safe=False,
)
