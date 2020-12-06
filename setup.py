
from setuptools import setup, find_packages

VERSION = 0.1

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='restaurant',
    version=VERSION,
    description='Simple commandline restaurant ordering system',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='',
    author_email='',
    url='https://github.com/author/restaurant/',
    license='unlicensed',
    package_data={'restaurant': ['res/*', 'database/*']},
    include_package_data=True,
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    entry_points="""
        [console_scripts]
        restaurant = restaurant.main:main
    """,
)
