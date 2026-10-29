PyAMS (Python for Analog and Mixed Signals)
===========================================

**PyAMS** is a Python library for modeling and simulating analog and mixed-signal
electronic circuits. You describe a circuit by connecting ready-made (or your own)
models through node names, choose an analysis — DC, transient or AC — run it, and
plot or post-process the results with NumPy and Matplotlib.

.. code-block:: sh

    pip install pyams-lib

.. code-block:: python

    from pyams.lib import circuit
    from pyams.models import Resistor, SinVoltage, Diode

    V1 = SinVoltage("In", "0");  V1.setParams("Va=10V Fr=2Hz")
    D1 = Diode("In", "Out")
    R1 = Resistor("Out", "0");   R1.setParams("R=1KΩ")

    cir = circuit()
    cir.addElements({"V1": V1, "D1": D1, "R1": R1})
    cir.setOutPuts("In", "Out")
    cir.analysis(mode="tran", start=0, stop=2, step=0.001)
    cir.run()
    cir.plot()

.. toctree::
   :maxdepth: 2
   :caption: Contents

   overview
   news
   release_history
   features
   installation
   modeling
   simulation
   options
   models/index
   examples/index
   api

Indices
-------

* :ref:`genindex`
* :ref:`search`
