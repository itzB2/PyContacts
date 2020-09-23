from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='vCard',
    version='1.0.0',
    description='Useful tools to work with VCF Cards in Python',
    long_description_content_type="text/markdown",
    long_description=README,
    license='MIT',
    packages=find_packages(),
    author='Judah Beethoven',
    author_email='masterofcoding@360@gmail.com',
    keywords=['vcf', 'VCFCard', 'VCFCard Python'],
    url='https://github.com/ncthuc/elastictools',
    download_url='https://pypi.org/project/elastictools/'
)

if __name__ == '__main__':
    setup(**setup_args)