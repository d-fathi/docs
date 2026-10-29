AC Current
==========

.. code-block:: python

    from pyams.models import ACCurrent

    X1 = ACCurrent("p", "n")
    X1.setParams("Idc=0 Iac=1")

Terminals
---------

``ACCurrent(p, n)``

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``Idc``
     - 0
     - A
     - DC value (bias)
   * - ``Iac``
     - 1
     - A
     - AC amplitude
   * - ``Ph``
     - 0
     - °
     - AC phase

Description
-----------

The documentation of the class (``help(ACCurrent)``)::

    Current source for the AC (small-signal frequency) analysis.

    In DC and transient analyses it is a constant source  I = Idc  (0 A by
    default).  In  ``analysis(mode="ac", ...)``  it injects the phasor
    Iac * exp(j Ph) at every frequency.  Direction as in DCCurrent: a positive
    current flows through the source from node p to node n.

    Attributes:
        I (signal): Current through the source, from p to n.
        Idc (param): DC value in Amperes (default 0 A).
        Iac (param): AC amplitude in Amperes (default 1 A).
        Ph (param): AC phase in degrees (default 0).

Used in the examples
--------------------

* :doc:`Dependent (controlled) sources: VCVS, CCVS, VCCS, CCCS </examples/dependent_sources>`

