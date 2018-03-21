Python Client Generator
=======================

|release level|

    API client generator for Python 3.

This is a proof-of-concept generator for API client libraries for APIs
specified by `protocol buffers`_, such as those inside Google.
It takes a service descriptor (as provided by `api-compiler`_) and uses it
to generate a client library.

.. _protocol buffers: https://developers.google.com/protocol-buffers/
.. _api-compiler: https://github.com/googleapis/api-compiler

Purpose
-------

This library primarily exists to facilitate experimentation, particularly
regarding:

  - An explicit normalized format for specifying APIs.
  - Lighter weight, in-language code generators.

Installation
------------

.. warning::

    This tool *only* runs on Python 3.6 or newer.
    (If you need Python 3.6, consider using `pyenv`_ to install it.)

The recommended method to install this library is using `pipsi`_.

.. code-block:: shell

    # Due to its experimental state, this tool is not published to a
    # package manager, and pip can not install from git-on-borg;
    # you should clone it.
    git clone sso://team/apiclient-eng/python-client-generator
    cd python-client-generator/

    # Install the tool. This will handle the virtualenv for you, and
    # make an appropriately-aliased executable.
    # The `--editable` flag is only necessary if you want to work on the
    # tool (as opposed to just use it).
    pipsi install --editable --python=`which python3.6` .

.. _pyenv: https://github.com/pyenv/pyenv
.. _pipsi: https://github.com/mitsuhiko/pipsi

Usage
-----

This tool expects as its input a "service descriptor", which is the output
of `api-compiler`_ (which itself requires a ``FileDescriptorSet`` proto
message, which one makes with `protoc`_).

.. note::

    If you just want to experiment, and feel like going through the steps
    to get one of these is a pain, feel free to use these pre-built
    `Vision descriptors`_.

    You want the binary descriptor (although the JSON one should work too),
    which is ``vision/descriptors/vision_service.desc``.
    There are also compiled protobuf files, which the resulting client
    library needs.

Run the tool with my unintuitively-named ``pyacf`` command, passing the
descriptor as a positional argument. In order to get a client library dumped
out to your disk, use the ``--output-dir`` flag.

.. code-block:: shell

    pyacf vision_service.desc --output-dir /path/to/output/

The client library that this outputs is not entirely complete; it also
relies on the compiled protocol buffer files from ``protoc``. You will need
to compile them and output them in the same directory.

Install the client library as normal. Note that you will need to install
``grpcio`` into the client library's virtualenv as well -- it will not
currently install it automatically (this is intentional) and it will not work,
even in HTTP mode, without it (this is not intentional and is due to some
minor structural fixes needed in ``api_core``).

.. _Vision descriptors: https://goto.google.com/api-client-tools-inputs
.. _protoc: https://github.com/google/protobuf

Features and Limitations
------------------------

Nice things this client does:

  - Implemented in pure Python, with language-idiomatic templating tools.
  - It supports multiple transports: both gRPC and protobuf over HTTP/1.1.
    A JSON-based transport would be easy to add.

As this is experimental work, please note the following limitations:

  - The output only works on Python 3.4 and above.
  - gRPC must be installed even if you are not using it (this is due to
    some minor issues in ``api-core``).
  - Only unary calls are implemented at this point.
  - No support for GAPIC features (e.g. LRO, method argument flattening) yet.
  - No tests are implemented.

.. |release level| image:: https://img.shields.io/badge/release%20level-pre%20alpha-red.svg?style&#x3D;flat
    :target: https://cloud.google.com/terms/launch-stages
