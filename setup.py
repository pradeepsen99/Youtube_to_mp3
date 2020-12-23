from setuptools import setup, find_packages

setup(
    name="Youtube_to_mp3",
    version="0.3.4",
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