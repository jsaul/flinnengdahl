from distutils.core import setup
from distutils.extension import Extension

inc_d = [
    'src'
]

ext = Extension(
    '_flinnengdahl',
    [
        'src/flinnengdahl_wrap.cpp',
        'src/fe.cpp'
    ],
    include_dirs=inc_d
)

setup(
    name='flinnengdahl',
    ext_modules=[ext],
    package_dir={'': 'src'},
    packages=[''],
    version='0.1.0',
    author='Joachim Saul',
    description='Python/C++ module to compute Flinn-Engdahl regions',
    license='AGPLv3',
)
