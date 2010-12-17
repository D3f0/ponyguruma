from distutils.core import setup, Extension
setup(
    name="ponyguruma",
    packages=['ponyguruma'],
    package_dir = {'': 'lib'},
    ext_modules=[
        Extension("ponyguruma._lowlevel", ["lib/ponyguruma/_lowlevel.c"],
                  library_dirs=['/usr/local/lib'],
                  libraries=['onig'])])
