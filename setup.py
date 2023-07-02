import setuptools


with open('README.md', 'r') as fh:
    long_description = fh.read()

DEV_REQUIREMENTS = [
    'bandit == 1.7.*',
    'black == 23.*',
    'build == 0.7.*',
    'flake8 == 6.*',
    'isort == 5.*',
    'mypy == 1.3.*',
    'pytest == 7.*',
    'pytest-cov == 4.*',
    'twine == 4.*',
]

setuptools.setup(
    name='pretty-tables',
    version='3.0.0',
    description='Create pretty tables from headers and rows, perfect for console output.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/justintime50/pretty-tables',
    author='Justintime50',
    license='MIT',
    packages=setuptools.find_packages(
        exclude=[
            'examples',
            'test',
        ]
    ),
    package_data={
        'pretty_tables': [
            'py.typed',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    extras_require={
        'dev': DEV_REQUIREMENTS,
    },
    python_requires='>=3.8, <4',
)
