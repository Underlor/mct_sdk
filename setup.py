import setuptools

setuptools.setup(
    name='mct_sdk',
    version='0.1.0',
    author="IO-HOST DEV",
    author_email="admin@1-0.su",
    url="https://github.com/Underlor/mct_sdk",
    description="MCT python SKD",
    install_requires=['requests', ],
    packages=setuptools.find_packages(),
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),
)
