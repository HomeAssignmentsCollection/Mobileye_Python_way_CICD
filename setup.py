#!/usr/bin/env python3
"""
Setup script for Product Delivery Pipeline.
"""

from setuptools import setup, find_packages

# Read requirements from requirements.txt
with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]

# Read development requirements (optional)
try:
    with open("code-quality/requirements-dev.txt", "r", encoding="utf-8") as f:
        dev_requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]
except FileNotFoundError:
    dev_requirements = []

setup(
    name="product-delivery-pipeline",
    version="0.1.0",
    description="A product delivery pipeline for building, deploying, and notifying about product releases",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/product-delivery-pipeline",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.9",
    install_requires=requirements,
    extras_require={
        "dev": dev_requirements,
    },
    entry_points={
        "console_scripts": [
            "product-pipeline=product_pipeline.main:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="pipeline, deployment, ci-cd, automation",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/product-delivery-pipeline/issues",
        "Source": "https://github.com/yourusername/product-delivery-pipeline",
        "Documentation": "https://github.com/yourusername/product-delivery-pipeline#readme",
    },
)
