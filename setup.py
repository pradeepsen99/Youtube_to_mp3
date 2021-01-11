from setuptools import setup, find_packages
from scripts.__version__ import __version__

setup(
    name="Youtube_to_mp3",
    author="Pradeep Senthil",
    author_email="https://github.com/pradeepsen99",
    maintainer="Arnas Amankavicius",
    maintainer_email="https://github.com/ArnasAmankavicius",
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.6",
    entry_points={"console_scripts": ["audiodl=scripts.main:convert"]},
    install_requires=[
        "click>=7.1.2,<8.0.0",
        "pydub>=0.24.1,<1.0.0",
        "pytube>=10.1.0,<11.0.0",
    ]
)