import pathlib
from setuptools import setup


HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="sotrace",
    version="1.0.3",
    description="Get and open StackOverflow posts for your tracebacks.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/SuperMaZingCoder/sotrace",
    author="SuperMaZingCoder",
    author_email="supermazingcoder@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    packages=["sotrace"],
    include_package_data=True,
)

