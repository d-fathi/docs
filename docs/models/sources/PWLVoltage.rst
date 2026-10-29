Piece-wise Linear Voltage
=========================

.. code-block:: python

    from pyams.models import PWLVoltage

    X1 = PWLVoltage("p", "n")
    X1.setParams("Td=0 Scale=1")

Terminals
---------

``PWLVoltage(p, n, points=None)``

Optional constructor arguments: ``points`` (default ``None``).

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``Td``
     - 0
     - s
     - Delay
   * - ``Scale``
     - 1
     - –
     - Amplitude scale
   * - ``Voff``
     - 0
     - V
     - Offset
   * - ``Rep``
     - 0
     - –
     - Repeat (1) or single shot (0)

Description
-----------

The documentation of the class (``help(PWLVoltage)``)::

    Piece-wise linear voltage source (SPICE ``PWL``): the voltage is defined by
    a list of (time, value) points and linearly interpolated between them.

        V(t) = Scale * pwl(t - Td) + Voff

    Before the first point it holds the first value, after the last point it
    holds the last value. Two points with the same time make a vertical step.
    With Rep = 1 the waveform between the first and last points repeats.

    Terminals: PWLVoltage(p, n)   (V(p) - V(n) = V)
    Points can be given in the constructor or later:
        V1 = PWLVoltage("a", "0", points=[(0, 0), (1e-3, 5), (2e-3, 5), (3e-3, 0)])
        V1.setPoints("0 0, 1m 5, 2m 5, 3m 0")        # SI prefixes allowed
    Parameters:
        Td    delay (s)             (0)
        Scale amplitude factor      (1)
        Voff  offset (V)            (0)
        Rep   1 = repeat, 0 = once  (0)
    The DC (operating point) value is the waveform value at t = 0.

Used in the examples
--------------------

* :doc:`PWL sources: arbitrary waveform from (time, value) points </examples/pwl_sources>`

