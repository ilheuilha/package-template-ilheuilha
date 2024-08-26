from setuptools import setup, find_packages


with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()


setup(
    name="package_python",
    version="0.0.1",
    author="ilheuilha",
    author_email="teste@teste.com",
    description="pequeno programa para verificar tipos de investimentos",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ilheuilha/package-template-ilheuilha.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.8",
)
