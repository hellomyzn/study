from setuptools import setup, find_packages

setup(
    name = 'python_programming_demo_app',
    version='0.0.2',
    packages=find_packages(),
    packages_data={'roboter': ['template/*.txt']},
    url='http://sakaijyunsoccer.appspot.com',
    license='MIT',
    author='jsakai',
    author_email='example@example.com',
    install_requires=['termcolor==1.1.0'],
    description='roboter description',
    test_suits='tests',
)
