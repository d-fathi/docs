Models
======

PyAMS ships ready-made models of the most common electronic elements. Every model is a class of ``pyams.models``; it is created with the names of the nodes its terminals are connected to, and its parameters are set with ``setParams()``.

.. code-block:: python

    from pyams.models import Resistor, DCVoltage, Diode

    R1 = Resistor("In", "Out")     # terminals p, n
    R1.setParams("R=4.7KΩ")
    print(R1.getParams())

``help(Resistor)`` prints the documentation of a model, including its equations.

.. toctree::
   :maxdepth: 2

   basic/index
   sources/index
   semiconductor/index
   ics/index
