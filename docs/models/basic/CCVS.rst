Current-Controlled Voltage Source (CCVS)
========================================

.. code-block:: python

    from pyams.models import CCVS

    X1 = CCVS("p", "n", "cp", "cn")
    X1.setParams("Rm=1000")

Terminals
---------

``CCVS(p, n, cp, cn)``

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``Rm``
     - 1000
     - Ω
     - Transresistance

Description
-----------

The documentation of the class (``help(CCVS)``)::

    Current-controlled voltage source (SPICE "H" element, a transresistance):

        v(p) - v(n) = Rm * Ic

    Ic is the current that flows through the control branch from cp to cn.  The
    control branch is built into the element: it is a zero-volt source, an
    ideal ammeter, so connect (cp, cn) IN SERIES with the branch whose current
    controls the source (the current enters at cp and leaves at cn).

    Typical uses: a current-to-voltage (transimpedance) converter, a gyrator,
    the primary-current sensing half of an ideal transformer.

    Terminals: CCVS(p, n, cp, cn).

    Attributes:
        Vs (signal): the 0 V sensing branch between cp and cn.
        Ic (signal): its current, from cp to cn.
        V  (signal): output voltage v(p) - v(n).
        Rm (param): transresistance in ohms (default 1 kΩ).

Used in the examples
--------------------

* :doc:`Dependent (controlled) sources: VCVS, CCVS, VCCS, CCCS </examples/dependent_sources>`

