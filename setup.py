#!/usr/bin/env python3
"""Setup configuration for VoidCore."""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text() if readme_file.exists() else ""

setup(
    name="voidcore",
    version="1.0.0",
    description="Ultra-extreme token compression extension for Gemini CLI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="papertop221",
    author_email="",
    url="https://github.com/papertop221/voidcore",
    license="MIT",
    
    py_modules=["voidcore_core", "voidcore_cli_wrapper"],
    
    entry_points={
        "console_scripts": [
            "voidcore=voidcore_cli_wrapper:main",
            "voidcore-cli=voidcore_cli_wrapper:main",
        ],
    },
    
    python_requires=">=3.8",
    install_requires=[
        "click>=8.1.0",
        "google-generativeai>=0.3.0",
        "python-dotenv>=0.21.0",
    ],
    
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    
    keywords="token compression gemini cli api gpt compression",
)
