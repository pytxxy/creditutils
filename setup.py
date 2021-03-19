from setuptools import setup, find_packages


with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()


setup(
    name='creditutils',
    version='0.2.4',
    author='liuzhy',
    author_email='liuzhy@tianxiaxinyong.com',
    description='python small tools util.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    url='https://github.com/pytxxy/creditutils',
    install_requires=[
        'paramiko>=2.7.2',
        'xmltodict>=0.11.0',
        'chardet>=3.0.4',
        'xlrd>=1.1.0',
        'pypng>=0.0.18',
        'GitPython>=3.1.11',
        'Pillow>=6.0.0'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
