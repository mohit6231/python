from setuptools import setup, find_packages

setup(
    name='test_package',
    version='0.1',
    description='A simple test package',
    author='Mohit Bansal',
    author_email='mohit.bansal@axelerant.com',
    url='https://github.com/mohit6231/python3/test_package',
    packages=find_packages(),
    install_requires=[
        # List your package dependencies here, e.g.,
        # 'numpy',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
