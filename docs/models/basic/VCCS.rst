Voltage-Controlled Current Source (VCCS)
========================================

.. code-block:: python

    from pyams.models import VCCS

    X1 = VCCS("p", "n", "cp", "cn")
    X1.setParams("Gm=0.001")

Terminals
---------

``VCCS(p, n, cp, cn)``

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``Gm``
     - 0.001
     - S
     - Transconductance

Description
-----------

The documentation of the class (``help(VCCS)``)::

    Voltage-controlled current source (SPICE "G" element, a transconductance):

        i(p -> n) = Gm * ( v(cp) - v(cn) )

    The current Gm*Vc flows through the source from p to n (it is taken out of
    node p and pushed into node n), like DCCurrent.  The control port draws no
    current.  Typical uses: the gm*vgs generator of a small-signal transistor
    model, a transconductance amplifier, a gyrator (two VCCS with opposite
    signs make an inductor from a capacitor).

    Terminals: VCCS(p, n, cp, cn).

    Attributes:
        Vc (signal): control voltage v(cp) - v(cn)  (input, no current).
        I  (signal): output current from p to n.
        Gm (param): transconductance in siemens (default 1 mS).

Used in the examples
--------------------

* :doc:`Dependent (controlled) sources: VCVS, CCVS, VCCS, CCCS </examples/dependent_sources>`

