import os
from codecs import open
from setuptools import setup
from setuptools.command import develop, build_py
import subprocess


here = os.path.abspath(os.path.dirname(__file__))

module = 'ponomarenko'

about = {}
with open(os.path.join(here, "__about__.py"), "r", "utf-8") as f:
    exec(f.read(), about)

def readme():
    with open(os.path.join(here, 'README.md'), 'r', 'utf-8') as f:
        return f.read()

class CustomDevelop(develop.develop, object):
    """
    Class needed for "pip install -e ."
    """
    def run(self):
        subprocess.check_call("(cd ponomarenko && make lib)", shell=True)
        super(CustomDevelop, self).run()


class CustomBuildPy(build_py.build_py, object):
    """
    Class needed for "pip install ponomarenko"
    """
    def run(self):
        subprocess.check_call("(cd ponomarenko && make lib)", shell=True)
        libdir = os.path.join(self.build_lib, module)
        self.mkpath(libdir)
        subprocess.check_call("cp -r ponomarenko/libpono.so {}".format(libdir), shell=True)
        super(CustomBuildPy, self).run()

requirements = ['numpy>=1.12']

setup(name=about["__title__"],
      version=about["__version__"],
      description=about["__description__"],
      long_description=readme(),
      long_description_content_type='text/markdown',
      url=about["__url__"],
      author=about["__author__"],
      author_email=about["__author_email__"],
      py_modules=[module],
      install_requires=requirements,
      python_requires=">=3.5",
      cmdclass={'develop': CustomDevelop,
                'build_py': CustomBuildPy},
      entry_points="""
          [console_scripts]
          ponomarenko=ponomarenko:cli
      """)

