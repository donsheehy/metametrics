import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="metametrics",
    version="0.1.0",
    author="Donald R. Sheehy",
    author_email="don.r.sheehy@gmail.com",
    description="A package for computing distances in metric spaces",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/donsheehy/metametrics",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[],
    entry_points='''
        [console_scripts]
        metametrics=metametrics.cli:cli
    ''',

)
