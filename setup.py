from distutils.core import setup

setup(
    name='py3njection',
    packages=['py3njection'],  # this must be the same as the name above
    version='0.1.1',
    description='A dependency injection module using python 3 annotations',
    long_description=open('README.rst').read(),
    author='Julien Tellier',
    author_email='julien.pascal.tellier@gmail.com',
    maintainer='Julien Tellier',
    maintainer_email='julien.pascal.tellier@gmail.com',
    url='https://github.com/Aigrefin/py3njection',
    download_url='https://github.com/Aigrefin/py3njection/tarball/0.1',
    license='BSD New',
    keywords=[
        'dependency',
        'injection',
        'annotation',
        'inject',
        'di',
        'dependency injection',
        'dependency injector',
        'dependency management',
        'ioc',
        'inversion of control'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
