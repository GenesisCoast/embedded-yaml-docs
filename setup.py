from setuptools import setup

setup(
    name='yaml_ci_docs',
    version='0.1.7',
    packages=[
        'yaml_ci_docs',
        'yaml_ci_docs.wrappers',
    ],
    package_dir={
        'yaml_ci_docs': 'src'
    },
    url='https://github.com/GenesisCoast/yaml_ci_docs',
    license='MIT',
    author='Harry Sanderson',
    author_email='harrysanderson@hotmail.co.uk',
    description='conditions-py is a library that helps write pre- and postcondition validations in a fluent manner, helping improve the readability and reliability of code.',
    long_description=open('README.md').read(),
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