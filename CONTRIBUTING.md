# Contributing


We are thrilled that you are interested in contributing to this project.
Please open an issue or pull request with your ideas.

# Running the tests


1. Follow the [local installation guide] to install `protoc` and `pandoc`.

2. Install and run [GAPIC Showcase].

3. Automated testing for testing is managed by [nox].

    To use nox, install it globally with `pip`:
    ```
    $ pip install nox
    ```

    To run all the tests:
    ```
    $ nox
    ```

    To run a specific test specify the session name:
    ```
    nox -s unit-3.7
    ```

[local installation guide]: https://gapic-generator-python.readthedocs.io/en/stable/getting-started/local.html#installing
[GAPIC Showcase]: https://github.com/googleapis/gapic-showcase#installation
[nox]: https://nox.readthedocs.io

# Contributor License Agreements


Before we can accept your pull requests, you will need to sign a Contributor
License Agreement (CLA):

- **If you are an individual writing original source code** and **you own the
  intellectual property**, then you'll need to sign an
  [individual CLA](https://developers.google.com/open-source/cla/individual)
- **If you work for a company that wants to allow you to contribute your work**,
  then you'll need to sign a
  [corporate CLA](https://developers.google.com/open-source/cla/corporate>)

You can sign these electronically (just scroll to the bottom). After that,
we'll be able to accept your pull requests.
