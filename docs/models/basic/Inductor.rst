Inductor
========

.. code-block:: python

    from pyams.models import Inductor

    X1 = Inductor("p", "n")
    X1.setParams("L=0.001")

Terminals
---------

``Inductor(p, n)``

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``L``
     - 0.001
     - H
     - Inductor value

Description
-----------

The documentation of the class (``help(Inductor)``)::

    This class implements an Inductor model.

    An inductor stores energy in a magnetic field and the voltage across it is
    proportional to the rate of change of its current.

    Attributes:
        I (signal): Input current signal through the inductor, defined between nodes (p, n).
        V (signal): Output voltage signal across the inductor, defined between nodes (p, n).
        L (param): Inductance value in Henries (H), default is 1.0e-3 H.

    Methods:
        analog(): Defines the inductor behavior using the equation:
                  V = L * dI/dt

    Note: the inductor imposes the voltage V, so its current is an extra unknown
    of the circuit (the 'in' current signal reads it).  In a DC analysis
    dI/dt = 0, so the inductor behaves as a short circuit.

Used in the examples
--------------------

* :doc:`Series RLC circuit (inductor example) </examples/rlc>`
* :doc:`AC analysis (small-signal frequency response) </examples/ac_analysis>`
* :doc:`Elliptic (Cauer) RLC low-pass filter </examples/elliptic_filter>`
* :doc:`Dependent (controlled) sources: VCVS, CCVS, VCCS, CCCS </examples/dependent_sources>`
* :doc:`IGBT chopper (low-side switch, inductive load, freewheel diode) </examples/igbt_chopper>`
* :doc:`Tunnel diode oscillator </examples/tunnel_diode_oscillator>`
* :doc:`Chua's circuit with op-amps (double-scroll chaotic oscillator) </examples/chua_opamp>`

