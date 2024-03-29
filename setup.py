from setuptools import setup, find_packages
    
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setup(
    name="utils-package-Martin36",
    version="0.0.8",
    author="Martin Funkquist",
    author_email="martin.funkquist@gmail.com",
    description="A package containing helpful util functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Martin36/utils_package",
    project_urls={
        "Bug Tracker": "https://github.com/Martin36/utils_package/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
    install_requires = [
        "jsonlines>=2.0.0"
    ]
)