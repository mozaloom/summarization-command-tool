from setuptools import setup, find_packages

with open("requirements.txt", "r", encoding="utf-16") as _f:
    requirements = [line.strip() for line in _f if line.strip()]

setup(
    name="summarize",
    version="1.0.0",
    description="Summarizes text using HuggingFace Transformers",
    author="Mohammed Zaloom",
    entry_points={"console_scripts": ["summarize = summarize.main:main"]},
    install_requires=requirements,
    packages=find_packages(),
)
