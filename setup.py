from setuptools import find_packages, setup, Extension

setup(
    name='flinnengdahl',
    version='1.0.4',
    author='Joachim Saul',
    description='Python/C++ module to compute Flinn-Engdahl regions',
    license='AGPLv3',

    packages=find_packages('src'),
    package_dir={'': 'src'},

    ext_modules = [
        Extension(
            name='flinnengdahl/_flinnengdahl',
            sources = [
                'src/flinnengdahl/flinnengdahl_wrap.cpp',
                'src/flinnengdahl/fe.cpp'
            ],
            include_dirs = [
                'src/flinnengdahl'
            ]
)
        ],
)
