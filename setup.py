from setuptools import setup, find_packages

setup(
    name="md2steam",
    version="1.1.0",
    packages=find_packages(),
    install_requires=["markdown-it-py"],
    python_requires=">=3.10",
    description="Markdown to Steam BBCode converter",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/YifeiDevs/md2steam",
    author="YifeiDevs (Forked from Andrey Kataev)",
)
