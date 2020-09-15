import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Languages", # Replace with your own username
    version="1.3.0",
    author="Aswanth Vc",
    author_email="no-mail@mail.no",
    description="Programming language decoder. Now You can Decode HyperTextMarkupLanguage (html) and css(Style sheet) using this package.",
    keywords=["html","hypertextmarkup decoder","programming language decoder","languages decoder","programming language decoder","super fast html decoder","html parser","css","style sheet","decoder","css decoder","style sheet decoder","python pip","languages pip"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aswanthabam/Language",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)