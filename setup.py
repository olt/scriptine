import scriptine
import os

name = "scriptine"
version = scriptine.__version__

class zipdist(scriptine.misc.DistutilsCommand):
    def run(self):
        from scriptine.meta import zipdist_command
        zipdist_command()

options = scriptine.misc.Options(
    name = name,
    version = version,
    author = "Oliver Tonnhofer",
    author_email = "olt@omniscale.de",
    description = 'python shell scripts made easy',
    long_description=open('README.txt').read() +'\n' + open('CHANGELOG.txt').read(),
    license = 'MIT License',
    classifiers=[
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python',
      ],
    packages = ['scriptine'],
    zip_safe = False,
    cmdclass = {
        'zipdist': zipdist,
    }
)

if __name__ == '__main__':
    try:
        from setuptools import setup
    except ImportError:
        from distutils.core import setup
    setup(**options)
