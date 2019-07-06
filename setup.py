from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='baseball_id',
      version='0.0.6',
      description='Lookup baseball players by their ID at various data ' +
                  'sources like MLB, Yahoo!, CBS, ESPN, and FanGraphs.',
      long_description=readme(),
      url='http://github.com/spilchen/baseball_id',
      author='Matt Spilchen',
      author_email='matt.spilchen@gmail.com',
      license='MIT',
      packages=['baseball_id'],
      setup_requires=["pytest-runner"],
      tests_require=["pytest"],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.7',
      ],
      install_requires=['pandas'],
      python_requires='>=3',
      include_package_data=True,
      zip_safe=True)
