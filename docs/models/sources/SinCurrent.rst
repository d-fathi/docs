Sinusoidal Current
==================

.. code-block:: python

    from pyams.models import SinCurrent

    X1 = SinCurrent("p", "n")
    X1.setParams("Fr=100 Ia=0.001")

Terminals
---------

``SinCurrent(p, n)``

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``Fr``
     - 100
     - Hz
     - Frequency of sine wave
   * - ``Ia``
     - 0.001
     - A
     - Amplitude of sine wave
   * - ``Ph``
     - 0
     - °
     - Phase of sine wave
   * - ``Ioff``
     - 0
     - A
     - Current offset

Description
-----------

The documentation of the class (``help(SinCurrent)``)::

    This class models a Sinusoidal Current Source.

    The current waveform follows the equation:
        I(t) = Ia * sin(2π * Fr * t + Ph) + Ioff

    A positive current flows through the source from node p to node n
    (SPICE convention, see DCCurrent).

    Attributes:
        I (signal): Current through the source, from p to n.
        Fr (param): Frequency of the sine wave (Hz).
        Ia (param): Amplitude of the sine wave (A).
        Ph (param): Phase shift in degrees (°).
        Ioff (param): Current offset (A).

    Methods:
        analog(): Implements the sinusoidal current equation.

Used in the examples
--------------------

* :doc:`Current sources: DCCurrent, SinCurrent, TrapezoidCurrent </examples/current_sources>`

