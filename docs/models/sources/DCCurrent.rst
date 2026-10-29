DC Current
==========

.. code-block:: python

    from pyams.models import DCCurrent

    X1 = DCCurrent("p", "n")
    X1.setParams("Idc=0.001")

Terminals
---------

``DCCurrent(p, n)``

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
     - 0.001
     - A
     - Constant current value

Description
-----------

The documentation of the class (``help(DCCurrent)``)::

    This class models a constant (DC) current source.

    The current is  I = Idc  at all times, whatever the voltage across it
    (a bias current, a charging current, the tail current of a pair ...).

    Direction (same as the SPICE source "I p n"): a positive current flows
    through the source from node p to node n, i.e. it is taken out of node p
    and pushed into node n.  A source from "0" to "x" with Idc > 0 therefore
    raises the voltage of node x.

    Attributes:
        I (signal): Current through the source, from p to n.
        Idc (param): Current value in Amperes (A), default is 1 mA.

    Methods:
        analog(): Implements the equation I = Idc.

Used in the examples
--------------------

* :doc:`Current sources: DCCurrent, SinCurrent, TrapezoidCurrent </examples/current_sources>`
* :doc:`Thyristor I(V) with several gate currents (IG0 ... IG3) </examples/thyristor_iv_family>`
* :doc:`UJT relaxation oscillator </examples/ujt_oscillator>`

