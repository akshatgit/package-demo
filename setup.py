from setuptools import setup, find_packages
setup(name='package',
      version='0.1',
      description='Demonstrate Python Packaging Process',
      url='https://github.com/akshatgit/package-demo',
      author='Akshat Sinha',
      author_email='akshat14132@iiitd.ac.in ',
      license='MIT',
      packages=["package"],
      install_requires=['numpy>=1.11',
                        'matplotlib>=1.5'])