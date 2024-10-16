from setuptools import setup, Extension

setup(
    name='flinnengdahl',
    version='1.0.2',
    author='Joachim Saul',
    description='Python/C++ module to compute Flinn-Engdahl regions',
    license='AGPLv3',
    
    ext_modules = [
        Extension(
            name='_flinnengdahl',
            sources = [
                'src/flinnengdahl_wrap.cpp',
                'src/fe.cpp'
            ],
            include_dirs = [
                'src'
            ]
)
        ],
    py_modules = ["flinnengdahl"],
)
