import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="minj",
    version="0.0.1",
    author="Guilherme Lowa",
    author_email="guilhermelowa@protonmail.com",
    description="Minimalist Journal on CLI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/guilhermelowa/minj",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "minj = minj.main:main"
        ]
    },
    python_requires='>=3.6',
)
