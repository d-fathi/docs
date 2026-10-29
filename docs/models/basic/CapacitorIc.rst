Capacitor with Initial Voltage
==============================

.. code-block:: python

    from pyams.models import CapacitorIc

    X1 = CapacitorIc("p", "n")
    X1.setParams("C=1e-06 Ic=0")

Terminals
---------

``CapacitorIc(p, n)``

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 18 18 18 46

   * - Name
     - Default
     - Unit
     - Description
   * - ``C``
     - 1e-06
     - F
     - Capacitance
   * - ``Ic``
     - 0
     - V
     - Initial voltage

Description
-----------

The documentation of the class (``help(CapacitorIc)``)::

    Capacitor with an initial voltage (SPICE ``C ... IC=``).

        V(t) = Ic + (1/C) integral(I dt)          (I flows p -> n)

    The capacitor is written in integral form: in the operating point at the
    start of a transient the integral is zero, so the capacitor is held at V = Ic
    (like ``.ic``/UIC in SPICE) and then evolves freely.  Use it together with
    InductorIc and a normal transient analysis (do not use ``uic=True``).

    Terminals: CapacitorIc(p, n)
    Parameters:
        C    capacitance (F)           (1 uF)
        Ic   initial voltage V(p)-V(n) (V)   (0)

Used in the examples
--------------------

* :doc:`Van der Pol oscillator:  C v'' + Mu (v^2 - 1) v' + v/L = 0 </examples/van_der_pol>`
* :doc:`Van der Pol oscillator: parametric sweep of Mu with cir.sweep(param="R1.Mu", list=[...]) </examples/van_der_pol_sweep>`

