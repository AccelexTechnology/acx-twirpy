from setuptools import setup, find_packages

with open("README.md") as f:
    readme = f.read()

with open("requirements.txt") as f:
    install_requires = f.read().splitlines()


setup(
      name="acx-twirpy",
      version="0.1.dev0",
      description="Twirp server and client lib",
      long_description=readme,
      long_description_content_type='text/markdown',
      license='unlicense',
      packages=find_packages(where="src"),
      package_dir={"": "src"},
      install_requires=install_requires,
      python_requires=">=3.8",
      zip_safe=True
      )
