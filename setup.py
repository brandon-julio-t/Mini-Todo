from setuptools import setup

setup(
    name='mini_todo',
    packages=['mini_todo'],
    install_requires=[
        'flask',
        'flask_migrate',
        'flask_sqlalchemy',
        'wtforms'
    ],
)