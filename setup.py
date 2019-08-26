import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


def get_install_requires():
    with open("requirements.txt", "r") as requirements_file:
        res = requirements_file.readlines()
        return [req.split(" ", maxsplit=1)[0] for req in res if req]


setuptools.setup(
    name="prom_mt",
    version="0.0.1",
    author="M T",
    description="A small python api to collect data from prometheus",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TeplovM/prom_api",
    install_requires=get_install_requires(),
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
