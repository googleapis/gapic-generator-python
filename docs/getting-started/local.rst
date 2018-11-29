.. _getting-started/local:

Local Installation
==================

If you are just getting started with code generation for protobuf-based APIs,
or if you do not have a robust Python environment already available, it is
probably easier to get started using Docker: :ref:`getting-started/docker`

However, this tool offers first-class support for local execution using
``protoc``. It is still reasonably easy, but initial setup will take a bit
longer.

.. note::

    If you are interested in contributing, setup according to these steps
    is recommended.


Installing
----------

protoc
~~~~~~

This tool is implemented as a plugin to the `protocol buffers`_ compiler, so
in order to use it, you will need to have the ``protoc`` command available.

The `release page`_ on GitHub contains the download you need.

.. note::

  You may notice both packages that designate languages (e.g.
  ``protobuf-python-X.Y.Z.tar.gz``) as well as packages that
  designate architectures (e.g. ``protoc-X.Y.Z-linux-x86_64.zip``). You want
  the one that designates an architecture; your goal here is to have a CLI
  command.

.. _protocol buffers: https://developers.google.com/protocol-buffers/
.. _release page: https://github.com/google/protobuf/releases

It is likely preferable to install ``protoc`` somewhere on your shell's path,
but this is not a strict requirement (as you will be invoking it directly).
``protoc`` is also quirky about how it handles well-known protos; you probably
also want to copy them into ``/usr/local/include``

To ensure it is installed propertly:

.. code-block:: shell

  $ protoc --version
  libprotoc 3.6.0


pandoc
~~~~~~

This generator relies on `pandoc`_ to convert from Markdown (the *lingua
franca* for documentation in protocol buffers) into ReStructured Text (the
*lingua franca* for documentation in Python).

Install this using an appropriate mechanism for your operating system.
Multiple installation paths are documented on the `pandoc installation page`_.

.. _pandoc: https://pandoc.org/
.. _pandoc installation page: https://pandoc.org/installing.html


API Generator for Python
~~~~~~~~~~~~~~~~~~~~~~~~

This package is provided as a standard Python library, and can be installed
the usual ways. It fundamentally provides a CLI command,
``protoc-gen-python_gapic``, (yes, the mismatch of ``kebob-case`` and
``snake_case`` is weird, sorry), so you will want to install using a mechanism
that is conducive to making CLI commands available.

Additionally, this program currently only runs against Python 3.6 or
Python 3.7, so you will need that installed. (Most Linux distributions ship
with earlier versions.) Use `pyenv`_ to get Python 3.7 installed in a
friendly way.

As for this library itself, the recommended installation approach is
`pipsi`_.

.. code-block:: shell

    # Due to its experimental state, this tool is not published to a
    # package manager; you should clone it.
    # (You can pip install it from GitHub, not not if you want to tinker.)
    git clone git@github.com:googleapis/gapic-generator-python.git
    cd gapic-generator-python/

    # Install the tool. This will handle the virtualenv for you, and
    # make an appropriately-aliased executable.
    # The `--editable` flag is only necessary if you want to work on the
    # tool (as opposed to just use it).
    pipsi install --editable --python=`which python3.7` .

To ensure the tool is installed properly:

.. code-block:: shell

  $ which protoc-gen-python_gapic
  /path/to/protoc-gen-python_gapic

.. _pyenv: https://github.com/pyenv/pyenv
.. _pipsi: https://github.com/mitsuhiko/pipsi

Usage
-----

To use this plugin, you will need an API which is specified using a
protocol buffer. Additionally, this plugin makes some assumptions at the
margins according to `Google API design conventions`_, so following those
conventions is recommended.

Example
~~~~~~~

If you want to experiment with an already-existing API, one example is
available. (Reminder that this is still considered experimental, so apologies
for this part being a bit strange.)

You need to clone the `googleapis`_ repository from GitHub, and change to
a special branch:

.. code-block:: shell

  $ git clone git@github.com:googleapis/googleapis.git
  $ cd googleapis
  $ git checkout --track -b input-contract origin/input-contract
  $ cd ..

The API available as an example (thus far) is the `Google Cloud Vision`_ API,
available in the ``google/cloud/vision/v1/`` subdirectory. This will be used
for the remainder of the examples on this page.

You will also need the common protos, currently in experimental status,
which define certain client-specific annotations. These are in the
`api-common-protos`_ repository. Clone this from GitHub also:

.. code-block:: shell

  $ git clone git@github.com:googleapis/api-common-protos.git
  $ cd api-common-protos
  $ git checkout --track -b input-contract origin/input-contract
  $ cd ..

.. _googleapis: https://github.com/googleapis/googleapis/tree/input-contract
.. _api-common-protos: https://github.com/googleapis/api-common-protos/tree/input-contract
.. _Google Cloud Vision: https://cloud.google.com/vision/


Compiling an API
~~~~~~~~~~~~~~~~

Compile the API into a client library by invoking ``protoc`` directly.
This plugin is invoked under the hood via. the ``--python_gapic_out`` switch.

.. code-block:: shell

  # This is assumed to be in the `googleapis` project root, and we also
  # assume that api-common-protos is next to it.
  $ protoc google/cloud/vision/v1/*.proto \
      --proto_path=../api-common-protos/ --proto_path=. \
      --python_gapic_out=/dest/

.. note::

  **A reminder about paths.**

  Remember that ``protoc`` is particular about paths. It requires all paths
  where it expects to find protos, and *order matters*. In this case,
  the common protos must come first, and then the path to the API being built.


Running a Client Library
~~~~~~~~~~~~~~~~~~~~~~~~

Once you have compiled a client library, it is time for the fun part:
actually running it!

Create a virtual environment for the library:

.. code-block:: shell

  $ virtualenv ~/.local/client-lib --python=`which python3.7`
  $ source ~/.local/client-lib/bin/activate

Next, install the library:

.. code-block:: shell

  $ cd /dest/
  $ pip install --editable .

Now it is time to play with it!
Here is a test script:

.. code-block:: python

  # This is the client library generated by this plugin.
  from google.cloud import vision

  # Instantiate the client.
  #
  # If you need to manually specify credentials, do so here.
  # More info: https://cloud.google.com/docs/authentication/getting-started
  #
  # If you wish, you can send `transport='grpc'` or `transport='http'`
  # to change which underlying transport layer is being used.
  ia = vision.ImageAnnotator()

  # Send the request to the server and get the response.
  response = ia.batch_annotate_images({
      'requests': [{
          'features': [{
              'type': vision.types.image_annotator.Feature.Type.LABEL_DETECTION,
          }],
          'image': {'source': {
              'image_uri': 'https://s3.amazonaws.com/cdn0.michiganbulb.com'
                           '/images/350/66623.jpg',
          }},
      }],
  })
  print(response)


.. _Google API design conventions: https://cloud.google.com/apis/design/
