import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="HyperTextMarkup", # Replace with your own username
    version="1.0.0",
    author="Aswanth Vc",
    author_email="no-mail@mail.com",
    description="Programming language decoder. Now You can Decode HyperTextMarkupLanguage (html) using this package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)