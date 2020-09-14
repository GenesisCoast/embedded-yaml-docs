from setuptools import setup

setup(
    name='embedded_yaml_docs',
    version='0.0.1',
    packages=[
        'embedded_yaml_docs',
        'embedded_yaml_docs.helpers',
        'embedded_yaml_docs.models',
        'embedded_yaml_docs.wrappers'
    ],
    package_dir={
        'embedded_yaml_docs': 'src'
    },
    url='https://github.com/GenesisCoast/embedded-yaml-docs',
    license='MIT',
    author='Harry Sanderson',
    author_email='harrysanderson@hotmail.co.uk',
    description='embedded_yaml_docs is a CLI used for generating markdown documentation, from your YAML files. This can be useful for documenting YAML files such as CI pipelines.',
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