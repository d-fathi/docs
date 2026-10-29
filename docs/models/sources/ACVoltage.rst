AC Voltage
==========

.. code-block:: python

    from pyams.models import ACVoltage

    X1 = ACVoltage("p", "n")
    X1.setParams("Vdc=0 Vac=1")

Terminals
---------

``ACVoltage(p, n)``

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``Vdc``
     - 0
     - V
     - DC value (bias)
   * - ``Vac``
     - 1
     - V
     - AC amplitude
   * - ``Ph``
     - 0
     - °
     - AC phase

Description
-----------

The documentation of the class (``help(ACVoltage)``)::

    Voltage source for the AC (small-signal frequency) analysis.

    In a DC or transient analysis it is a constant source  V = Vdc  (0 V by
    default, so the AC source is silent: it has no effect on the operating
    point).  In  ``analysis(mode="ac", ...)``  the circuit is linearised around
    its DC operating point and this source injects the phasor

        Vac * exp(j * Ph)

    at every frequency, so each node voltage of the result is directly the
    transfer function (with Vac = 1 V, the default).

    Attributes:
        V (signal): Output voltage between nodes (p, n); p is the + terminal.
        Vdc (param): DC value in Volts (default 0 V): the bias of the operating point.
        Vac (param): AC amplitude in Volts (default 1 V).
        Ph (param): AC phase in degrees (default 0).

    Methods:
        analog(): V = Vdc.
        ac(): the (signal name, phasor) pair used by the AC analysis.

Used in the examples
--------------------

* :doc:`RC low-pass: how to use analysis(mode="ac") </examples/rc_ac_simple>`
* :doc:`AC analysis (small-signal frequency response) </examples/ac_analysis>`
* :doc:`Elliptic (Cauer) RLC low-pass filter </examples/elliptic_filter>`
* :doc:`Dependent (controlled) sources: VCVS, CCVS, VCCS, CCCS </examples/dependent_sources>`

