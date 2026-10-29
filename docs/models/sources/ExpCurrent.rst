Exponential Current
===================

.. code-block:: python

    from pyams.models import ExpCurrent

    X1 = ExpCurrent("p", "n")
    X1.setParams("I1=0 I2=0.001")

Terminals
---------

``ExpCurrent(p, n)``

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``I1``
     - 0
     - A
     - Initial value
   * - ``I2``
     - 0.001
     - A
     - Pulsed value
   * - ``TD1``
     - 0.001
     - s
     - Rise delay time
   * - ``TAU1``
     - 0.001
     - s
     - Rise time constant
   * - ``TD2``
     - 0.005
     - s
     - Fall delay time
   * - ``TAU2``
     - 0.001
     - s
     - Fall time constant

Description
-----------

The documentation of the class (``help(ExpCurrent)``)::

    Exponential current source (SPICE ``EXP``); same waveform as ExpVoltage.
    The current I flows from p to n through the source.

    Terminals: ExpCurrent(p, n)
    Parameters:
        I1   initial value (A)                 (0)
        I2   pulsed value (A)                  (1 mA)
        TD1  rise delay time (s)               (1 ms)
        TAU1 rise time constant (s)            (1 ms)
        TD2  fall delay time (s)               (5 ms)
        TAU2 fall time constant (s)            (1 ms)
    The DC (operating point) value is I1.

Used in the examples
--------------------

* :doc:`Exponential sources (SPICE EXP): ExpVoltage drives an RC filter, ExpCurrent charges a capacitor </examples/exp_sources>`

