import humanstxt

doc = humanstxt.__doc__.replace("latest", "v%s" % humanstxt.__version__)

from setuptools import setup

setup(
    name='humanstxt',
    version=humanstxt.__version__,
    author='whtsky',
    author_email='whtsky@gmail.com',
    url='https://github.com/whtsky/humanstxt',
    py_modules=['humanstxt'],
    description='A python library for dealing with humans.txt',
    long_description=doc,
    include_package_data=True,
    license='MIT License',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ],
    tests_require=['nose'],
    test_suite='nose.collector',
)
