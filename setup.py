from setuptools import setup, find_packages

setup(
    name="my_library",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    description="A simple example library",
    author="Mohamed Luqman",
    author_email="luqmandepy@gmail.com",
    url="https://github.com/luqmancode",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
