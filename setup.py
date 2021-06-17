from setuptools import setup

with open("README.md", encoding="u8") as readme:
    long_description = readme.read()

setup(
  name = 'IsraeliQueue',
  version = '1.1',
  license='MIT',
  description = 'A Python module that allows the usage of Israeli Queue',
  author = 'Yon Liud',
  author_email = 'ejliud@gmail.com',
  long_description=long_description,
  long_description_content_type="text/markdown",
  url = 'https://github.com/YonLiud/Israeli-Queue',
  keywords = ['Israel','IsraeliQueue', 'Tools', 'Queue'],
  classifiers=[
    'Development Status :: 3 - Alpha',	
    'Intended Audience :: Developers',
    'Topic :: Utilities',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
  ],
)
