Piece-wise Linear Current
=========================

.. code-block:: python

    from pyams.models import PWLCurrent

    X1 = PWLCurrent("p", "n")
    X1.setParams("Td=0 Scale=1")

Terminals
---------

``PWLCurrent(p, n, points=None)``

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
   * - ``Ioff``
     - 0
     - A
     - Offset
   * - ``Rep``
     - 0
     - –
     - Repeat (1) or single shot (0)

Description
-----------

The documentation of the class (``help(PWLCurrent)``)::

    Piece-wise linear current source (SPICE ``PWL``); same behaviour as
    PWLVoltage. The current flows from p to n through the source.

        I(t) = Scale * pwl(t - Td) + Ioff

    Terminals: PWLCurrent(p, n)
        I1 = PWLCurrent("0", "a", points="0 0, 1m 2m, 2m 2m, 3m 0")   # A, SI prefixes allowed
    Parameters: Td (s), Scale, Ioff (A), Rep (1 = repeat).

Used in the examples
--------------------

* :doc:`PWL sources: arbitrary waveform from (time, value) points </examples/pwl_sources>`

