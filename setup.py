from setuptools import setup, find_packages

# Read the contents of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="nirspersion",
    version="0.1.0",
    author="Darío González Picos",
    author_email="dariogonzalezpicos@gmail.com",
    description="Instrumental broadening of JWST NIRSpec with custom resolving power profiles.",
    python_requires='>=3.6',
)
