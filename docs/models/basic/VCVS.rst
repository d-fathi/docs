Voltage-Controlled Voltage Source (VCVS)
========================================

.. code-block:: python

    from pyams.models import VCVS

    X1 = VCVS("p", "n", "cp", "cn")
    X1.setParams("Gain=1")

Terminals
---------

``VCVS(p, n, cp, cn)``

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``Gain``
     - 1
     - V/V
     - Voltage gain

Description
-----------

The documentation of the class (``help(VCVS)``)::

    Voltage-controlled voltage source (SPICE "E" element):

        v(p) - v(n) = Gain * ( v(cp) - v(cn) )

    The control port (cp, cn) draws no current.  The output port (p, n) is an
    ideal voltage source, so its current is set by the circuit around it.
    Typical uses: an ideal amplifier or buffer, an op-amp with a finite gain
    (Gain = 1e5), the secondary of an ideal transformer.

    Terminals: VCVS(p, n, cp, cn).

    Attributes:
        Vc (signal): control voltage v(cp) - v(cn)  (input, no current).
        V  (signal): output voltage v(p) - v(n).
        Gain (param): voltage gain, V/V (default 1).

Used in the examples
--------------------

* :doc:`Dependent (controlled) sources: VCVS, CCVS, VCCS, CCCS </examples/dependent_sources>`

