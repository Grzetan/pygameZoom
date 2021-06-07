from setuptools import setup

with open("README.md", "r") as f:
    description = f.read()

setup(
    name='pygameZoom',
    version='0.0.3',
    description='Zoom into pygame figures without quality loss',
    long_description=description,
    long_description_content_type="text/markdown",
    py_modules=['pygameZoom'],
    package_dir={"": "src"},
    classifiers=[
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.7",
        "Topic :: Games/Entertainment :: Simulation",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    install_requires=[
        "pygame"
    ],
    url="https://github.com/Grzetan/pygameZoom",
    author="Grzegorz Paleta",
    author_email="grzetan@gmail.com"
)
