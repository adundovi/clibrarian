from setuptools import find_packages, setup

setup(name="clibrarian",
      version="0.1",
      description="Command line interface for different library tools",
      author="Andrej Dundovic",
      author_email='andrej@dundovic.com.hr',
      platforms=["linux"],
      license="BSD",
      url="",
      keywords="cli library books arxiv physics",
      packages=find_packages(),
      install_requires=['lxml>=3.6.0', 'mako>=1.0.0'],
      entry_points={
          'console_scripts': [
              'clibrarian = clibrarian.__main__:main'
          ]
      },
     )
