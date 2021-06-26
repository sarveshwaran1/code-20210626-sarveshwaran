import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="BMICalculator",
    version="1.0.0",
    author="Sarveshwaran J",
    author_email="sarveshwaranj@gmail.com",
    description="BMI Calculator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="<https://github.com/sarveshwaranj/BMICalculator>",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)