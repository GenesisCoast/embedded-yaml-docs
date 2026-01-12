from setuptools import setup, find_packages

with open('requirements.txt', mode='r', encoding='utf-8') as f:
    requirements = f.read().splitlines()

with open('README.md', mode='r', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='embedded-yaml-docs',
    version='1.0.1',
    packages=find_packages(),
    package_dir={
        'embedded-yaml-docs': 'src'
    },
    entry_points='''
        [console_scripts]
        embedded-yaml-docs=src.cli:cli
    ''',
    url='https://github.com/GenesisCoast/embedded-yaml-docs',
    license='MIT',
    install_requires=requirements,
    author='Harry Sanderson',
    author_email='harrysanderson@hotmail.co.uk',
    description='embedded_yaml_docs is a CLI used for generating markdown documentation, from your YAML files. This can be useful for documenting YAML files such as CI pipelines.',
    long_description=readme,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        # 'Topic :: Software Development :: Libaries :: Application Frameworks',
        # 'Topic :: Software Development :: Libaries :: Python Modules',
        # 'Topic :: Software Development :: Quality Assurance',
        # 'Topic :: Utilities'
    ]
)
