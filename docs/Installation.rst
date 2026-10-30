Installation
============

There are two ways to use PyAMS:

* as a **Python library** (``pyams-lib``), installed with pip, or
* inside the **CAD system** (the PyAMS application or the VS Code extension).

Requirements
------------

* Python 3.8 or later (CPython or PyPy), on Linux, Windows or macOS
* `NumPy <https://numpy.org>`_ and `Matplotlib <https://matplotlib.org>`_

Install as a Python library
---------------------------

.. code-block:: sh

    pip install pyams-lib

NumPy and Matplotlib are installed automatically. The names ``pyams-lib`` and ``pyams_lib``
are equivalent for pip.

To upgrade to the latest version:

.. code-block:: sh

    pip install --upgrade pyams-lib

Use a virtual environment (recommended)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: sh

    python -m venv .venv
    source .venv/bin/activate        # Windows: .venv\Scripts\activate
    pip install pyams-lib

Install the CAD system
----------------------

The CAD system lets you design circuits (schematic capture), design symbols and run simulations.
Choose one of the following:

1. **PyAMS application:** download it from https://pyams.sf.net.
2. **PyAMS extension for VS Code:** install it from the VS Code Extensions view.

.. note::

   The PyAMS application and the VS Code extension already include the ``pyams`` library,
   so you do **not** need to install it with pip. You only need Python with the
   ``numpy`` and ``matplotlib`` packages:

   .. code-block:: sh

       pip install numpy matplotlib