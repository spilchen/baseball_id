from setuptools import setup

setup(name='baseball_id',
      version='0.0.1',
      description='Lookup a players to find their ID at various data sources',
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
      zip_safe=False)
