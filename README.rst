API Client Generator for Python
===============================

|release level|

    A generator for protocol buffer described APIs for and in Python 3.

This is a proof-of-concept generator for API client libraries for APIs
specified by `protocol buffers`_, such as those inside Google.
It takes a protocol buffer (with particular annotations) and uses it
to generate a client library.

.. _protocol buffers: https://developers.google.com/protocol-buffers/

Purpose
-------

This library primarily exists to facilitate experimentation, particularly
regarding:

  - An explicit normalized format for specifying APIs.
  - Lighter weight, in-language code generators.

Documentation
-------------

For more information, see the ``docs/`` directory. (Start on ``index.rst``.)

You can build the docs into a nice HTML page. This requires installing
`Sphinx`_; once this is done, just run ``make html`` from within the
``docs/`` directory.

.. _Sphinx: https://sphinx-doc.org/

Disclaimer
----------

This is not an official Google product.


.. |release level| image:: https://img.shields.io/badge/release%20level-pre%20alpha-red.svg?style&#x3D;flat
    :target: https://cloud.google.com/terms/launch-stages
