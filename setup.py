from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()

setup(
    name='autility',
    version='0.1',
    description='A useful module',
    license="MIT",
    long_description=long_description,
    author='DDD',
    author_email='secret',
    url="OK",
    packages=['autility'],  # same as name
    install_requires=['pandas', 'plotly'],  # external packages as dependencies
    scripts=[
        'scripts/plot_something',
    ]
)
