
import setuptools


VERSION = '0.0.1'


with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()


setuptools.setup(
    name='thanachart',
    version=VERSION,
    author='Thanachart Ritbumroong',
    author_email='thanachart.rit@gmail.com',  # TODO: update email
    description='Personal package for Thanachart',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/happilyeverafter95/pdf-wrangler',
    install_requires=['chardet==3.0.4', 'pdfminer.six==20181108'],
    project_urls={
        'Main': 'https://github.com/thanachart/thanachart',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    python_requires='>=3.6',
)