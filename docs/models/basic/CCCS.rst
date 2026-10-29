Current-Controlled Current Source (CCCS)
========================================

.. code-block:: python

    from pyams.models import CCCS

    X1 = CCCS("p", "n", "cp", "cn")
    X1.setParams("Gain=1")

Terminals
---------

``CCCS(p, n, cp, cn)``

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
     - A/A
     - Current gain

Description
-----------

The documentation of the class (``help(CCCS)``)::

    Current-controlled current source (SPICE "F" element, a current mirror /
    current amplifier):

        i(p -> n) = Gain * Ic

    Ic is the current that flows through the control branch from cp to cn.  The
    control branch is built into the element: it is a zero-volt source, an
    ideal ammeter, so connect (cp, cn) IN SERIES with the branch whose current
    controls the source (the current enters at cp and leaves at cn).  The
    output current Gain*Ic flows through the source from p to n.

    Typical uses: the beta*ib generator of a transistor model, an ideal current
    mirror, the primary current of an ideal transformer.

    Terminals: CCCS(p, n, cp, cn).

    Attributes:
        Vs (signal): the 0 V sensing branch between cp and cn.
        Ic (signal): its current, from cp to cn.
        I  (signal): output current from p to n.
        Gain (param): current gain, A/A (default 1).

Used in the examples
--------------------

* :doc:`Dependent (controlled) sources: VCVS, CCVS, VCCS, CCCS </examples/dependent_sources>`

