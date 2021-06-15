import setuptools

with open("README.md", encoding="u8") as readme:
    long_description = readme.read()


setuptools.setup(
    name="Israeli-Queue",
    version="1.0.0",
    author="YonLiud",
    author_email="ejliud@gmail.com",
    description="A python module for Israeli queues",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YonLiud/Israeli-Queue",
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: System :: Logging",
    ],
    python_requires=">=3"
)
