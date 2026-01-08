"""
Setup script for LJPW Autopoiesis Module.

Self-healing Python script engine based on LJPW Framework V7.9.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ljpw-autopoiesis",
    version="0.1.0",
    author="LJPW Framework Contributors",
    description="Self-healing Python script engine based on LJPW Framework V7.9",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BruinGrowly/LJPW-Autopoiesis-Module",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Quality Assurance",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "ljpw-heal=ljpw_autopoiesis.cli:main",
        ],
    },
)
