Installation
============

Requirements
------------

* Python 3.8 or later (CPython or PyPy), on Linux, Windows or macOS
* `NumPy <https://numpy.org>`_ and `Matplotlib <https://matplotlib.org>`_ (installed automatically)

Install with pip
----------------

.. code-block:: sh

    pip install pyams-lib

The names ``pyams-lib`` and ``pyams_lib`` are equivalent for pip.

To upgrade to the latest version:

.. code-block:: sh

    pip install --upgrade pyams-lib

Use a virtual environment (recommended)
---------------------------------------

.. code-block:: sh

    python -m venv .venv
    source .venv/bin/activate        # Windows: .venv\Scripts\activate
    pip install pyams-lib

Check the installation
----------------------

.. code-block:: python

    from pyams.lib import circuit
    from pyams.models import Resistor, DCVoltage

    V1 = DCVoltage("In", "0");  V1.setParams("Vdc=12V")
    R1 = Resistor("In", "Out"); R1.setParams("R=2KΩ")
    R2 = Resistor("Out", "0");  R2.setParams("R=1KΩ")

    cir = circuit()
    cir.addElements({"V1": V1, "R1": R1, "R2": R2})
    cir.setOutPuts("Out")
    cir.analysis(mode="dc")
    print(cir.run()["Out"][0])       # 4.0

Install from source
-------------------

.. code-block:: sh

    git clone https://github.com/d-fathi/pyams_lib
    cd pyams_lib
    pip install .

Note that the package is imported as ``pyams`` (``from pyams.lib import circuit``)
although it is installed as ``pyams-lib``.
