from pathlib import Path
from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="togax-xml-layout-plugin",
    description="XML unofficial Toga layout parser",
    long_description=Path("README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    url="https://github.com/sinedie/togax-xml-layout-plugin",
    version="0.0.1",
    author="EAR",
    author_email="sinedie@protonmail.com",
    license="FREE",
    python_requires=">=3.6",
    install_requires=requirements,
    packages=find_packages(),
    keywords=["python", "toga", "gui", "xml", "layout"],
)
