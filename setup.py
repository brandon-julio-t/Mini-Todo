from setuptools import setup, find_packages

setup(
    name='mini-todo',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'flask_migrate',
        'flask_sqlalchemy',
        'wtforms'
    ],
)