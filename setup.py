import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pymarkauth", # Replace with your own username
    version="0.0.1",
    author="Hendrik Lankers",
    author_email="hendrik.lankers.hl@googlemail.com",
    description="Generate markdown using Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/elsholz/PyMarkAuth",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
