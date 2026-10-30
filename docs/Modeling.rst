Modeling (method)
=================

The modeling of analog elements in ``pyams.lib`` is based on describing their behavior in the
Python language, following a structured approach:

1. Declare the required library.
2. Define the model name (a class derived from ``model``).
3. Declare the parameters with their default values.
4. Declare the signals (voltage or current) and connect them to the terminals.
5. Write the relationships between signals and parameters (the equations).

The general structure of an analog element is:

.. code-block:: python

   from pyams.lib import model, signal, param, voltage, current   # 1. library declaration

   class NameOfElement(model):                                    # 2. model definition

       def __init__(self, p, n):                                  # terminals (node names)
           self.V  = signal('in',  voltage, p, n)                 # 4. signals
           self.I  = signal('out', current, p, n)
           self.P1 = param(1.0, 'unit', 'Description')            # 3. parameters

       def analog(self):                                          # 5. equations
           self.I += ...

A first complete example, the resistor:

.. code-block:: python

   class Resistor(model):
       def __init__(self, p, n):
           self.V = signal('in',  voltage, p, n)       # V = v(p) - v(n)
           self.I = signal('out', current, p, n)       # current flowing from p to n
           self.R = param(1000.0, 'Ω', 'Resistance')

       def analog(self):
           self.I += self.V / self.R                   # Ohm's law

The ``__init__`` and ``analog`` functions
-----------------------------------------

``__init__`` receives the **terminals** (node names), creates the signals that connect the element
to the circuit and sets the default values of the parameters. ``analog`` defines the mathematical
relationships between signals and parameters: it is the *behavioral model* of the element.
These two functions are the core of every model.

Signals and parameters
----------------------

A **signal** represents an electrical quantity (voltage or current) attached to two terminals:

.. code-block:: python

   signal(direction, kind, p, n)

where:

- ``direction`` is ``'in'`` (the solver writes the value, ``analog()`` reads it) or ``'out'`` (``analog()`` contributes to it).
- ``kind`` is ``voltage`` or ``current``.
- ``p`` and ``n`` are the positive and negative terminals.

A **parameter** is a constant that influences the behavior of the element. It can be changed
from outside with ``setParams()``:

.. code-block:: python

   param(value, unit, description)

where:

- ``value`` is the default value of the parameter.
- ``unit`` is its unit of measurement.
- ``description`` is a short explanation of the parameter.

Allowed operations between signals and parameters
-------------------------------------------------

Inside ``analog()``, signals, parameters and ``time`` behave like plain floats. The following
operations are available:

============  ====================================  =========
Operation     Description                           Result
============  ====================================  =========
``+``         addition                              real
``-``         subtraction                           real
``*``         multiplication                        real
``/``         division                              real
``**``        exponentiation                        real
``==``        test for equality                     boolean
``!=``        test for inequality                   boolean
``<``         test for less than                    boolean
``<=``        test for less than or equal           boolean
``>``         test for greater than                 boolean
``>=``        test for greater than or equal        boolean
``+=``        add a contribution to an output       –
              signal (``self.I += x``)
============  ====================================  =========

Functions of the ``math`` module (``exp``, ``sin``, ``log``, …) can be applied to them directly.

Signal declarations
-------------------

The four possible declarations of ``signal(direction, kind, p, n)``:

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Declaration
     - Meaning
   * - ``signal('in', voltage, p, n)``
     - the value of ``v(p) - v(n)``; read it inside ``analog()``
   * - ``signal('out', current, p, n)``
     - ``sig += x`` adds a current ``x`` flowing from ``p`` to ``n`` through the element
       (KCL: it leaves node ``p`` and enters node ``n``)
   * - ``signal('out', voltage, p, n)``
     - ``sig += x`` imposes ``v(p) - v(n) = x`` (an ideal voltage source); the current through it
       becomes an extra unknown
   * - ``signal('in', current, p, n)``
     - the current of the ``('out', voltage)`` signal that sits on the same two nodes
       (used by current-controlled elements)

Inside ``analog()`` signals, parameters and ``time`` behave like plain floats, so ``math.exp``,
``math.sin``, … can be applied to them directly.

Writing your own model
----------------------

A diode, written with the Shockley equation:

.. code-block:: python

    from math import exp
    from pyams.lib import model, signal, param, voltage, current

    class MyDiode(model):
        def __init__(self, p, n):
            self.V = signal('in',  voltage, p, n)     # read:  V = v(p) - v(n)
            self.I = signal('out', current, p, n)     # write: current p -> n
            self.Is = param(1e-14,   'A', 'Saturation current')
            self.Vt = param(0.02585, 'V', 'Thermal voltage')

        def analog(self):
            self.I += self.Is * (exp(self.V / self.Vt) - 1)

It is used exactly like a built-in element:

.. code-block:: python

    V1 = DCVoltage("In", "0");  V1.setParams("Vdc=5V")
    R1 = Resistor("In", "A");   R1.setParams("R=1KΩ")
    D1 = MyDiode("A", "0")

    cir = circuit()
    cir.addElements({"V1": V1, "R1": R1, "D1": D1})
    cir.setOutPuts("A", "D1.I")
    cir.analysis(mode="dc")
    print(cir.run())

Building a circuit
------------------

An element is created with the names of the nodes its terminals are connected to.
Two terminals that use the same node name are connected together. The names ``"0"``,
``"gnd"`` and ``"ground"`` all mean the reference node.

.. code-block:: python

    R1 = Resistor("In", "N1")      # between node In and node N1
    C1 = Capacitor("N1", "0")      # between node N1 and ground

Elements are added to a ``circuit`` as a dictionary ``{name: element}``. The element name is
used later to select parameters and signals (for example ``"R1.R"`` or ``"D1.I"``):

.. code-block:: python

    cir = circuit()
    cir.addElements({"V1": V1, "R1": R1, "C1": C1})

``setOutPuts`` selects what is recorded and plotted:

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Output name
     - Meaning
   * - ``"Out"``
     - voltage of the node ``Out``
   * - ``"R1.I"``
     - a signal of an element, written ``Element.signal`` (here the current of ``R1``)
   * - ``"R1.V"``
     - voltage across the element ``R1``

If ``setOutPuts`` is not called, all node voltages are recorded.

Setting parameters
------------------

Parameters are set with a string of ``name=value`` pairs. Values accept the engineering
prefixes ``T G Meg k m u n p f`` and an optional unit:

.. code-block:: python

    R1.setParams("R=4.7KΩ")
    V1.setParams("Va=5V Fr=50Hz")
    C1.setParams("C=100nF")
    L1.setParams(L=10e-3)                       # keyword arguments
    D1.setParams({"Iss": 1e-12, "n": 1.5})      # or a dictionary

``element.getParams()`` returns every parameter with its unit and description. An unknown
parameter name raises an error that lists the valid ones.

Time derivative and integral
----------------------------

``ddt(x)`` is the time derivative of ``x`` (it is 0 in a DC analysis) and ``idt(x)`` its time integral.
A capacitor is therefore simply:

.. code-block:: python

    from pyams.lib import ddt

    class MyCap(model):
        def __init__(self, p, n):
            self.V = signal('in',  voltage, p, n)
            self.I = signal('out', current, p, n)
            self.C = param(1e-6, 'F', 'Capacitance')

        def analog(self):
            self.I += self.C * ddt(self.V)

and an inductor can be written with the integral (see :doc:`examples/idt_example`).

The ``time`` object gives the simulation time inside ``analog()``, which is how time-dependent
sources are written:

.. code-block:: python

    from math import sin, pi
    from pyams.lib import time

    class MySource(model):
        def __init__(self, p, n):
            self.V = signal('out', voltage, p, n)
            self.Va = param(1.0, 'V', 'Amplitude')
            self.Fr = param(50.0, 'Hz', 'Frequency')

        def analog(self):
            self.V += self.Va * sin(2 * pi * self.Fr * time)

How the equations are solved
----------------------------

PyAMS uses *modified nodal analysis*: Kirchhoff's current law is written at every node and
the equations of the voltage sources are added as extra unknowns. The non-linear system is
solved by the **Newton–Raphson** method. The Jacobian is obtained by forward finite differences of
``analog()``, so a model only needs to state its equations — no derivative has to be coded.
If Newton's method fails to converge, the solver retries with limited node-voltage steps and
with *gmin stepping*; in a transient run a failing time step is bisected.